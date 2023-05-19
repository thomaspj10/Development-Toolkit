from dataclasses import dataclass
from devkit.generators.igenerator import IGenerator
from devkit.generators.base import DecoratorGenerator, ClassGenerator, FunctionGenerator
from devkit.generators.base.class_generator import ClassAttribute

@dataclass
class ForeignKey:
    table: str
    column: str
    nullable: bool

class SqlModelGenerator(IGenerator):
    
    __table: str
    __columns: list[ClassAttribute]
    __foreign_keys: list[ForeignKey]
    
    def __init__(self) -> None:
        super().__init__()
        self.__columns = []
        self.__foreign_keys = []
    
    def set_table(self, table: str):
        self.__table = table
    
    def add_column(self, name: str, type: str):
        self.__columns.append(ClassAttribute(name, type, None))
    
    def add_foreign_key(self, table_name: str, column: str, nullable: bool):
        self.__foreign_keys.append(ForeignKey(table_name, column, nullable))
    
    def generate(self, indent: int) -> str:
        class_generator = ClassGenerator()
        class_generator.set_name(self.__table)
        
        dataclass_decorator = DecoratorGenerator()
        dataclass_decorator.set_decorator("dataclass")
        dataclass_decorator.add_argument("slots", "True")
        dataclass_decorator.add_from_import("dataclasses", ["dataclass"])
        
        class_generator.add_decorator(dataclass_decorator)
        
        class_generator.add_inherited_class("Model")
        class_generator.add_from_import("devkit.sql", ["Model", "fetch_as"])
        class_generator.add_from_import("dataclasses", ["field"])
        
        # Attributes.
        class_generator.add_attribute("id", "int", "field(init=False, default=None) # type: ignore")
        for column in self.__columns:
            class_generator.add_attribute(column.name, column.type)
        
        # Default functions
        staticmethod_decorator = DecoratorGenerator()
        staticmethod_decorator.set_decorator("staticmethod")
        
        find_by_id_function = FunctionGenerator()
        find_by_id_function.set_name("find_by_id")
        find_by_id_function.set_body("""result = fetch_as(f"select rowid as id, * from `""" + self.__table + """` where `rowid` = {id}", """ + self.__table + """)

if len(result) == 0:
    return None
        
return result[0]""")
        find_by_id_function.set_return_type(f"{self.__table} | None")
        find_by_id_function.add_decorator(staticmethod_decorator)
        find_by_id_function.add_argument("id", "int")
        
        find_all_function = FunctionGenerator()
        find_all_function.set_name("find_all")
        find_all_function.set_body("""return fetch_as(f"select rowid as id, * from `""" + self.__table + """`", """ + self.__table + """)""")
        find_all_function.set_return_type(f"list[{self.__table}]")
        find_all_function.add_decorator(staticmethod_decorator)
        
        class_generator.add_function(find_by_id_function)
        class_generator.add_function(find_all_function)
        
        # Foreign key functions
        for foreign_key in self.__foreign_keys:
            foreign_key_function = FunctionGenerator()
            
            snake_case_table_name = ''.join(['_' + c.lower() if c.isupper() else c for c in foreign_key.table]).lstrip('_')
            foreign_key_function.set_name(f"get_{snake_case_table_name}")
            
            return_type = f"{foreign_key.table} | None" if foreign_key.nullable else foreign_key.table
            foreign_key_function.set_return_type(return_type)
            
            
            foreign_key_function.add_argument("self", "Self")
            foreign_key_function.add_from_import("typing", ["Self"])
            
            body = ""
            
            if foreign_key.nullable:
                body += f"""if self.{foreign_key.column} == None: 
    return None

"""

            body += f"return {foreign_key.table}.find_by_id(self.{foreign_key.column})" + ("" if foreign_key.nullable else " # type: ignore")
            
            foreign_key_function.set_body(body)

            class_generator.add_function(foreign_key_function)
        
        return class_generator.generate(indent)

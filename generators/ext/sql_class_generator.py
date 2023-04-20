from generators.igenerator import IGenerator
from generators.base import DecoratorGenerator, ClassGenerator, FunctionGenerator
from generators.base.class_generator import ClassAttribute

class SqlClassGenerator(IGenerator):
    
    __table: str
    __attributes: list[ClassAttribute]
    
    def __init__(self) -> None:
        super().__init__()
        self.__attributes = []
    
    def set_table(self, table: str):
        self.__table = table
    
    def add_attribute(self, name: str, type: str):
        self.__attributes.append(ClassAttribute(name, type, None))
    
    def generate(self, indent: int) -> str:
        class_generator = ClassGenerator()
        class_generator.set_name(self.__table)
        
        dataclass_decorator = DecoratorGenerator()
        dataclass_decorator.set_decorator("dataclass")
        dataclass_decorator.add_argument("slots", "True")
        dataclass_decorator.add_from_import("dataclasses", ["dataclass"])
        
        class_generator.add_decorator(dataclass_decorator)
        
        class_generator.add_inherited_class("Model")
        class_generator.add_from_import("sql", ["Model", "fetch_as"])
        class_generator.add_from_import("dataclasses", ["field"])
        
        class_generator.add_attribute("id", "int | None", "field(init=False, default=None)")
        for attribute in self.__attributes:
            class_generator.add_attribute(attribute.name, attribute.type)
        
        staticmethod_decorator = DecoratorGenerator()
        staticmethod_decorator.set_decorator("staticmethod")
        
        find_by_id_function = FunctionGenerator()
        find_by_id_function.set_name("find_by_id")
        find_by_id_function.set_body("""result = fetch_as(f"select * from `""" + self.__table + """` where `id` = {id}", """ + self.__table + """)

if len(result) == 0:
    return None
        
return result[0]
""")
        find_by_id_function.set_return_type(f"{self.__table} | None")
        find_by_id_function.add_decorator(staticmethod_decorator)
        find_by_id_function.add_argument("id", "int")
        
        find_all_function = FunctionGenerator()
        find_all_function.set_name("find_all")
        find_all_function.set_body("""return fetch_as(f"select * from `""" + self.__table + """`", """ + self.__table + """)""")
        find_all_function.set_return_type(f"list[{self.__table}]")
        find_all_function.add_decorator(staticmethod_decorator)
        
        class_generator.add_function(find_by_id_function)
        class_generator.add_function(find_all_function)
        
        return class_generator.generate(indent)

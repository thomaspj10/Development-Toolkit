from dataclasses import dataclass
from devkit.generators.igenerator import IGenerator
from devkit.generators.base.class_generator import ClassGenerator
from devkit.generators.base.raw_code_generator import RawCodeGenerator

@dataclass
class Column:
    name: str
    type: str

class SqlClassDefinitionGenerator(IGenerator):
    
    __table: str
    __columns: list[Column]
    
    def __init__(self) -> None:
        super().__init__()
        self.__columns = []
    
    def set_table(self, table: str):
        self.__table = table
    
    def add_column(self, name: str, type: str):
        self.__columns.append(Column(name, type))

    def generate(self, indent: int) -> str:
        class_name = f"{self.__table}Table"

        class_generator = ClassGenerator()
        class_generator.set_name(class_name)
        class_generator.add_inherited_class(f"TableDefinition[{self.__table}, '{class_name}']")

        class_generator.add_from_import("devkit.sql.querying", ["TableDefinition", "ColumnDefinition"])

        for column in self.__columns:
            class_generator.add_attribute(column.name.upper(), f"ColumnDefinition[{class_name}, {column.type}]", f"ColumnDefinition('{column.name}')")

        raw_code_generator = RawCodeGenerator()
        raw_code_generator.set_code(f"{self.__table.upper()} = {class_name}('{self.__table}', {self.__table})")

        return class_generator.generate(indent) + "\n" + raw_code_generator.generate(indent) + "\n"

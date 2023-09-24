import re
from dataclasses import dataclass
from devkit.generators.ext import SqlModelGenerator, SqlClassDefinitionGenerator
from devkit.generators.igenerator import IGenerator
from devkit.generators.python_file import python_file
import devkit.sql.database as database

@dataclass
class SqlColumn:
    name: str
    type: str
    nullable: bool

@dataclass
class SqlForeignKey:
    table: str
    column: str
    nullable: bool

def sql_type_to_python_type(sql_type: str) -> str:
    SQL_TO_PYTHON_TYPES = {
        "varchar": "str",
        "text": "str",
        "binary": "bytes",

        "smallint": "bool",
        "boolean": "bool",

        "int": "int",
        "float": "float"
    }
    
    for key, python_type in SQL_TO_PYTHON_TYPES.items():
        if key in sql_type:
            return python_type
        
    return ""

def generate_models():
    """
    Generate the Python classes which represent the tables in the database.
    """
    tables = database.fetch("select `sql` from sqlite_schema where `name` != 'sqlite_sequence'")

    regex = re.compile(r"CREATE TABLE (.*?) \((.*)\)", re.MULTILINE | re.S)

    generators: list[IGenerator] = []

    for table in tables:
        schema = table["sql"]
        columns: list[SqlColumn] = []
        foreign_keys: list[SqlForeignKey] = []
        
        match = regex.match(schema)

        if match != None:
            # Parse the sql schema string.
            table = match.group(1)
            columns_schema = match.group(2)
            
            for column_schema in columns_schema.split(","):
                column_schema = column_schema.strip()
                column_schema_split = column_schema.split(" ")
                
                # Get the data about this specific column.
                column_name = column_schema_split[0]
                column_type = sql_type_to_python_type(column_schema_split[1])
                column_nullable = not "not null" in column_schema
                
                # Parse the foreign key seperate.
                if column_schema.startswith("foreign key"):
                    foreign_key_match = re.match(r"foreign key \((.*?)\) references (.*?)\((.*)\)", column_schema)
                    
                    if foreign_key_match != None:
                        foreign_key_table = foreign_key_match.group(2)
                        foreign_key_column = foreign_key_match.group(1)
                        foreign_key_nullable = any([column.nullable for column in columns if column.name == foreign_key_column])
                        
                        foreign_keys.append(SqlForeignKey(foreign_key_table, foreign_key_column, foreign_key_nullable))
                        
                    continue
                
                columns.append(SqlColumn(column_name, column_type, column_nullable))
                
            # Create the model generator.
            model_generator = SqlModelGenerator()
            model_generator.set_table(table)
            for column in columns:
                # Ignore the id, because that is always generated.
                if column.name == "id":
                    continue

                model_generator.add_column(column.name, column.type + (" | None" if column.nullable else ""))

            for foreign_key in foreign_keys:
                model_generator.add_foreign_key(foreign_key.table, foreign_key.column, foreign_key.nullable)

            generators.append(model_generator)

            # Create the class definition generator.
            class_definition_generator = SqlClassDefinitionGenerator()
            class_definition_generator.set_table(table)
            for column in columns:
                class_definition_generator.add_column(column.name, column.type, column.nullable)

            generators.append(class_definition_generator)

    with python_file("models.py") as pf:
        pf.add_future_import("annotations")
        
        for generator in generators:
            pf.add_generator(generator)

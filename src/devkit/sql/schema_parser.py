import re
from dataclasses import dataclass
from devkit.generators.ext import SqlClassGenerator
from devkit.python_file import python_file
import devkit.sql as sql

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
        "int": "int"
    }
    
    for key, python_type in SQL_TO_PYTHON_TYPES.items():
        if key in sql_type:
            return python_type
        
    return ""

def generate_models():
    """
    Generate the Python classes which represent the tables in the database.
    """
    tables = sql.fetch("select `sql` from sqlite_schema where `name` != 'sqlite_sequence'")

    regex = re.compile(r"CREATE TABLE (.*?) \((.*)\)")

    generators: list[SqlClassGenerator] = []

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
                
                # Get the data about this specific schema.
                column_name = column_schema_split[0]
                column_type = sql_type_to_python_type(column_schema_split[1])
                column_nullable = not "not null" in column_schema
                
                # Ignore the id, because that is always generated.
                if column_name == "id":
                    continue
                
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
                
            # Create the generator.
            generator = SqlClassGenerator()
            generator.set_table(table)
            for column in columns:
                generator.add_column(column.name, column.type + (" | None" if column.nullable else ""))

            for foreign_key in foreign_keys:
                generator.add_foreign_key(foreign_key.table, foreign_key.column, foreign_key.nullable)

            generators.append(generator)
            
    with python_file("models.py") as pf:
        pf.add_future_import("annotations")
        
        for generator in generators:
            pf.add_generator(generator)

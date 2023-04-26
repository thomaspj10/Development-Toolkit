import devkit.sql as sql
# import models

sql.set_sqlite_file("database.db")

tables = sql.fetch("select `sql` from sqlite_schema where `name` != 'sqlite_sequence'")

import re
from dataclasses import dataclass
from devkit.generators.ext import SqlClassGenerator
from devkit.python_file import python_file

@dataclass
class SqlColumn:
    name: str
    type: str
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

regex = re.compile(r"CREATE TABLE (.*?) \((.*)\)")

generators: list[SqlClassGenerator] = []

for table in tables:
    schema = table["sql"]
    columns: list[SqlColumn] = []
    
    match = regex.match(schema)

    if match != None:
        # Parse the sql schema string.
        table = match.group(1)
        columns_schema = match.group(2)
        
        for column_schema in columns_schema.split(","):
            column_schema = column_schema.strip()
            column_schema_split = column_schema.split(" ")
            
            column_name = column_schema_split[0]
            column_type = sql_type_to_python_type(column_schema_split[1])
            column_nullable = not "not null" in column_schema
            
            if column_name == "id":
                continue
            
            if column_schema.startswith("foreign key"):
                continue
            
            columns.append(SqlColumn(column_name, column_type, column_nullable))
            
        # Create the generator.
        generator = SqlClassGenerator()
        generator.set_table(table)
        for column in columns:
            generator.add_column(column.name, column.type + (" | None" if column.nullable else ""))

        generators.append(generator)
        
with python_file("test.py") as pf:
    pf.add_future_import("annotations")
    
    for generator in generators:
        pf.add_generator(generator)

# sql.execute("drop table User")
# sql.execute("drop table Address")
# sql.execute("create table Address (id integer primary key autoincrement, name varchar(255))")
# sql.execute("create table User (id integer primary key autoincrement, name varchar(255), address_id int, foreign key (address_id) references User(id))")

# address = models.Address("Straat")

# user = models.User("Aap", address.id)
# user.store()

# for user in models.User.find_all():
#     address = user.get_address()
#     print(user)
#     print(address)

from __future__ import annotations
import sqlite3
from typing import Type, TypeVar, Any
from abc import ABC

connection: sqlite3.Connection

def set_sqlite_file(sqlite_file: str):
    global connection
    connection = sqlite3.connect(sqlite_file)
    connection.row_factory = sqlite3.Row

class Model(ABC):
    
    __is_new: bool = False
    
    def __post_init__(self):
        self.__is_new = True
    
    def store(self):
        """
        Creates a new row in the database if none exists, the row gets updated if it already exists.
        """
        if self.__is_new:
            self.__create()
            self.__is_new = False
        else:
            self.__update()
    
    def delete(self):
        """
        Delete this row from the database.
        """
        id = self.__getattribute__("id")
        
        sql = f"delete from `{self._get_table_name()}` where `id` = {id}"
        execute(sql)
    
    def _get_table_name(self) -> str:
        return self.__class__.__name__
    
    def __update(self):
        values: list[str] = []
        for annotation in get_class_annotations(self):
            value = self.__getattribute__(annotation)
            sql_value = python_to_sql_value(value)
            
            values.append(f"`{annotation}` = {sql_value}")
        
        values_string = ", ".join(values)
        id = self.__getattribute__("id")
        
        sql = f"update `{self._get_table_name()}` set {values_string} where `id` = '{id}'"
        execute(sql)
    
    def __create(self):
        values: list[str] = []
        for annotation in get_class_annotations(self):
            value = self.__getattribute__(annotation)
            values.append(python_to_sql_value(value))
                
        values_string = ", ".join(values)
        
        sql = f"insert into `{self._get_table_name()}` values ({values_string})"
        execute(sql)

T = TypeVar("T", bound=Model)

def execute(sql: str):
    """
    Execute a sql query.
    """
    print(f"[SQL] {sql}")
    cursor = connection.cursor()
    
    cursor.execute(sql)
    connection.commit()

def fetch(sql: str) -> list[sqlite3.Row]:
    """
    Fetch data from the database.
    """
    print(f"[SQL] {sql}")
    cursor = connection.cursor()
    
    cursor.execute(sql)
    
    return cursor.fetchall()

def fetch_as(sql: str, type: Type[T]) -> list[T]:
    """
    Fetch data from the database and convert it to a class instance.
    """
    return [create_class_instance(row, type) for row in fetch(sql)]

# Create a new class instance from a sqlite row.
def create_class_instance(row: sqlite3.Row, type: Type[T]) -> T:
    obj = type.__new__(type)
    
    for annotation in get_class_annotations(obj):
        value = row[annotation]
        obj.__setattr__(annotation, value)
        
    return obj

# Only public fields are valid for usage.
def get_class_annotations(model: Model):
    return [annotation for annotation in model.__annotations__ if not annotation.startswith("__")]

# Convert a Python value to sql value
# Examples:
# None -> null
# Hello -> 'Hello'
# 10 -> 10
def python_to_sql_value(value: Any) -> str:
    if value == None:
        return "null"
    
    if isinstance(value, str):
        return f"'{value}'"
    
    return str(value)

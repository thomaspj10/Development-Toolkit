from __future__ import annotations
import sqlite3
from typing import Type, TypeVar, Any
from abc import ABC

connection: sqlite3.Connection

def set_sqlite_file(sqlite_file: str):
    """
    Set the location of the sqlite database. This has to be done before any other sql operation.
    """
    global connection
    connection = sqlite3.connect(sqlite_file)
    connection.row_factory = sqlite3.Row

class Model(ABC):
    
    # Performance optimization to only make an actual sql query when the data has been modifed.
    __is_modified: bool
    
    def __post_init__(self):
        self.__create()
        self.__is_modified = False
    
    def __setattr__(self, attribute: str, value: Any):
        # Be careful: We have to do it this way to prevent a recursive call.
        super().__setattr__("_Model__is_modified", True)
        return super().__setattr__(attribute, value)
    
    def delete(self):
        """
        Delete this row from the database.
        """
        id = self.__getattribute__("id")
        
        sql = f"delete from `{self._get_table_name()}` where `id` = {id}"
        execute(sql)
    
    def _get_table_name(self) -> str:
        return self.__class__.__name__
    
    def store(self):
        """
        Stores the row into the database.
        """
        if not self.__is_modified:
            return
        
        keys: list[str] = []
        values: list[Any] = []
        for annotation in get_class_annotations(self):
            keys.append(f"`{annotation}` = ?")
            values.append(self.__getattribute__(annotation))
        
        keys_string = ", ".join(keys)
        id = self.__getattribute__("id")
        
        sql = f"update `{self._get_table_name()}` set {keys_string} where `id` = '{id}'"
        execute(sql, values)
    
    def __create(self):
        keys: list[str] = []
        values: list[Any] = []
        for annotation in get_class_annotations(self):
            keys.append("?")
            values.append(self.__getattribute__(annotation))
                
        keys_string = ", ".join(keys)
        
        sql = f"insert into `{self._get_table_name()}` values ({keys_string})"
        id = insert(sql, values)
        self.__setattr__("id", id)

T = TypeVar("T", bound=Model)

def execute(sql: str, parameters: list[str] = []):
    """
    Execute a sql query.
    """
    print(f"[SQL] {sql}")
    cursor = connection.cursor()
    
    cursor.execute(sql, parameters)
    connection.commit()

def insert(sql: str, parameters: list[str] = []) -> int | None:
    """
    Insert a row into the database and return the 
    """
    print(f"[SQL] {sql}")
    cursor = connection.cursor()
    
    cursor.execute(sql, parameters)
    connection.commit()
    return cursor.lastrowid

def fetch(sql: str, parameters: list[str] = []) -> list[sqlite3.Row]:
    """
    Fetch data from the database.
    """
    print(f"[SQL] {sql}")
    cursor = connection.cursor()
    
    cursor.execute(sql, parameters)
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

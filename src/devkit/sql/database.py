from __future__ import annotations
from typing import Type, TypeVar, Any
from abc import ABC
import devkit.logger as logger
import mysql.connector

_connection: mysql.connector.MySQLConnection | None = None
debug = False

def connect(host: str, port: int, database: str, user: str, password: str):
    global _connection
    _connection = mysql.connector.connect( # type: ignore
        host = host,
        port = port,
        user = user,
        password = password,
        database = database
    )

def get_connection() -> mysql.connector.MySQLConnection:
    if _connection != None:
        return _connection
    
    raise Exception("Attempting to execute a database query while not connected.")

def close_connection():
    """
    Close the connection to the sqlite database if any exists.
    """
    if _connection != None:
        _connection.close()

def set_debug(is_debug: bool):
    """
    Enable or disable debug mode which logs all sql queries to the console.
    """
    global debug
    debug = is_debug

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
            keys.append(f"`{annotation}` = %s")
            values.append(self.__getattribute__(annotation))
        
        keys_string = ", ".join(keys)
        id = self.__getattribute__("id")
        
        sql = f"update `{self._get_table_name()}` set {keys_string} where `id` = '{id}'"
        execute(sql, values)
    
    def __create(self):
        keys: list[str] = []
        values: list[Any] = []
        for annotation in get_class_annotations(self):
            keys.append("%s")
            values.append(self.__getattribute__(annotation))
                
        keys_string = ", ".join(keys)
        
        sql = f"insert into `{self._get_table_name()}` values ({keys_string})"
        id = insert(sql, values)
        self.__setattr__("id", id)

T = TypeVar("T", bound=Model)

def commit():
    get_connection().commit()

def rollback():
    get_connection().rollback()

def execute(query: str, parameters: list[Any] = []):
    """
    Execute a sql query.
    """
    if debug: logger.debug(f"[SQL] {query} - {parameters}")
    with get_connection().cursor() as cursor:    
        cursor.execute(query, parameters)
        commit()

def execute_script(sql_script: str):
    """
    Execute a sql query.
    """
    for query in sql_script.split(";"):
        if len(query.strip()) != 0:
            execute(query)

def insert(query: str, parameters: list[Any] = []) -> int | None:
    """
    Insert a row into the database and return the row id
    """
    if debug: logger.debug(f"[SQL] {query} - {parameters}")
    with get_connection().cursor() as cursor: 
        cursor.execute(query, parameters)
        commit()
    return cursor.lastrowid

def fetch(query: str, parameters: list[Any] = []) -> list[Any]:
    """
    Fetch data from the database.
    """
    if debug: logger.debug(f"[SQL] {query} - {parameters}")
    with get_connection().cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchall() # type: ignore

def fetch_as(query: str, type: Type[T], parameters: list[Any] = []) -> list[T]:
    """
    Fetch data from the database and convert it to a class instance.
    """
    return [create_model_instance(row, type) for row in fetch(query, parameters)]

def fetch_one(query: str, parameters: list[str] = []) -> Any | None:
    if debug: logger.debug(f"[SQL] {query} - {parameters}")
    with get_connection().cursor(buffered=True) as cursor:
        cursor.execute(query, parameters) 
        return cursor.fetchone()

def fetch_one_as(query: str, type: Type[T], parameters: list[str] = []) -> T | None:
    result = fetch_one(query, parameters)
    if result == None:
        return None
    return create_model_instance(result, type)

# Create a new class instance from a sqlite row.
def create_model_instance(row: Any, type: Type[T]) -> T:
    obj = type.__new__(type)
    
    for index, annotation in enumerate(get_class_annotations(obj)):
        value = row[index]
        obj.__setattr__(annotation, value)
        
    return obj

# Only public fields are valid for usage.
def get_class_annotations(model: Model):
    return [annotation for annotation in model.__annotations__ if not annotation.startswith("__")]

from __future__ import annotations
from typing import TypeVar, Generic, Any, Type
import models
import devkit.sql as sql

sql.set_sqlite_file("database.db")
sql.set_debug(True)

class QueryBuilder:
    
    __table_name: str
    __table_type: Type[Any]
    __conditions: list[Condition[Any, Any]]

    def __init__(self, table_name: str, table_type: Type[Any]) -> None:
        self.__table_name = table_name
        self.__table_type = table_type
        self.__conditions = []

    def add_condition(self, condition: Condition[Any, Any]):
        self.__conditions.append(condition)

    def get_parameters(self) -> list[Any]:
        parameters: list[Any] = []
        for condition_parameters in [item.parameters for item in self.__conditions]:
            for parameter in condition_parameters:
                parameters.append(parameter)

        return parameters

    def build(self) -> str:
        condition_string = " and ".join([item.condition for item in self.__conditions])
        if len(condition_string) > 0: condition_string = " where " + condition_string

        return f"select * from `{self.__table_name}`{condition_string}"
    
    def get_table_type(self) -> Type[Any]:
        return self.__table_type

T = TypeVar("T", bound=sql.Model)
U = TypeVar("U", bound="TableDefinition[Any, Any]")
V = TypeVar("V")
W = TypeVar("W")

class Condition(Generic[U, W]):

    condition: str
    parameters: list[Any]

    def __init__(self, condition: str, parameters: list[Any]) -> None:
        super().__init__()
        self.condition = condition
        self.parameters = parameters

class ColumnDefinition(Generic[U, W]):
    
    column_name: str

    def __init__(self, column_name: str) -> None:
        super().__init__()
        self.column_name = column_name

    def eq(self, other: W) -> Condition[U, W]:
        return Condition(f"(`{self.column_name}` = ?)", [other])

class TableDefinition(Generic[T, U]):
    
    table_name: str
    table_type: Type[T]

    def __init__(self, table_name: str, table_type: Type[T]) -> None:
        super().__init__()
        self.table_name = table_name
        self.table_type = table_type

class UserTable(TableDefinition[models.User, "UserTable"]):
    ID: ColumnDefinition[UserTable, int] = ColumnDefinition("id")
    NAME: ColumnDefinition[UserTable, str] = ColumnDefinition("name")

USER = UserTable("User", models.User)

class SelectFromStep(Generic[T, U]):
    
    __query_builder: QueryBuilder

    def __init__(self, query_builder: QueryBuilder) -> None:
        super().__init__()
        self.__query_builder = query_builder

    def where(self, condition: Condition[U, Any]) -> WhereStep[T, U]:
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def fetch(self) -> list[T]:
        return []

class WhereStep(Generic[T, U]):

    __query_builder: QueryBuilder

    def __init__(self, query_builder: QueryBuilder) -> None:
        super().__init__()
        self.__query_builder = query_builder

    def and_(self, condition: Condition[U, Any]) -> WhereStep[T, U]:
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def fetch(self) -> list[T]:
        sql_query = self.__query_builder.build()
        parameters = self.__query_builder.get_parameters()

        return sql.fetch_as(sql_query, self.__query_builder.get_table_type(), parameters)

def selectFrom(table: TableDefinition[T, U]) -> SelectFromStep[T, U]:
    return SelectFromStep(QueryBuilder(table.table_name, table.table_type))

result = selectFrom(USER).where(USER.ID.eq(1)).and_(USER.NAME.eq("Aap")).fetch()
print(result)

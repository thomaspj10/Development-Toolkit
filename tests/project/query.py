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

        return f"select rowid as id, * from `{self.__table_name}`{condition_string}"
    
    def get_table_type(self) -> Type[Any]:
        return self.__table_type

ModelType = TypeVar("ModelType", bound=sql.Model)
TableDefinitionType = TypeVar("TableDefinitionType", bound="TableDefinition[Any, Any]")
ParameterType = TypeVar("ParameterType")

class Condition(Generic[TableDefinitionType, ParameterType]):

    condition: str
    parameters: list[Any]

    def __init__(self, condition: str, parameters: list[Any]) -> None:
        super().__init__()
        self.condition = condition
        self.parameters = parameters

class ColumnDefinition(Generic[TableDefinitionType, ParameterType]):
    
    column_name: str

    def __init__(self, column_name: str) -> None:
        super().__init__()
        self.column_name = column_name

    def eq(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"(`{self.column_name}` = ?)", [other])
    
    def lt(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"(`{self.column_name}` < ?)", [other])

    def le(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"(`{self.column_name}` <= ?)", [other])
    
    def gt(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"(`{self.column_name}` > ?)", [other])
    
    def ge(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"(`{self.column_name}` >= ?)", [other])

class TableDefinition(Generic[ModelType, TableDefinitionType]):
    
    table_name: str
    table_type: Type[ModelType]

    def __init__(self, table_name: str, table_type: Type[ModelType]) -> None:
        super().__init__()
        self.table_name = table_name
        self.table_type = table_type

class UserTable(TableDefinition[models.User, "UserTable"]):
    ID: ColumnDefinition[UserTable, int] = ColumnDefinition("id")
    NAME: ColumnDefinition[UserTable, str] = ColumnDefinition("name")

USER = UserTable("User", models.User)

class AddressTable(TableDefinition[models.Address, "AddressTable"]):
    ID: ColumnDefinition[AddressTable, int] = ColumnDefinition("id")
    NAME: ColumnDefinition[AddressTable, str] = ColumnDefinition("name")

ADDRESS = AddressTable("Address", models.Address)

class SelectFromStep(Generic[ModelType, TableDefinitionType]):
    
    __query_builder: QueryBuilder

    def __init__(self, query_builder: QueryBuilder) -> None:
        super().__init__()
        self.__query_builder = query_builder

    def where(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[ModelType, TableDefinitionType]:
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def fetch(self) -> list[ModelType]:
        return []

class WhereStep(Generic[ModelType, TableDefinitionType]):

    __query_builder: QueryBuilder

    def __init__(self, query_builder: QueryBuilder) -> None:
        super().__init__()
        self.__query_builder = query_builder

    def and_(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[ModelType, TableDefinitionType]:
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def fetch(self) -> list[ModelType]:
        sql_query = self.__query_builder.build()
        parameters = self.__query_builder.get_parameters()

        return sql.fetch_as(sql_query, self.__query_builder.get_table_type(), parameters)

def selectFrom(table: TableDefinition[ModelType, TableDefinitionType]) -> SelectFromStep[ModelType, TableDefinitionType]:
    return SelectFromStep(QueryBuilder(table.table_name, table.table_type))

result = selectFrom(USER).where(USER.ID.le(1)).and_(USER.NAME.eq("Aap")).fetch()
print(result)

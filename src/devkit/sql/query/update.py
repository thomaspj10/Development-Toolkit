from __future__ import annotations
from devkit.sql.query.definitions import TableDefinition, ColumnDefinition, Condition, TableDefinitionType, ParameterType
import devkit.sql as sql
from typing import Generic, Any
from dataclasses import dataclass

@dataclass
class Update:
    column: str
    value: Any

class UpdateQueryBuilder:

    __table_name: str
    __updates: list[Update]
    __conditions: list[Condition[Any, Any]]

    def __init__(self, table_name: str) -> None:
        self.__table_name = table_name
        self.__updates = []
        self.__conditions = []

    def add_condition(self, condition: Condition[Any, Any]):
        self.__conditions.append(condition)

    def add_update(self, update: Update):
        self.__updates.append(update)

    def get_parameters(self) -> list[Any]:
        parameters: list[Any] = []

        for update in self.__updates:
            parameters.append(update.value)

        for condition_parameters in [item._parameters for item in self.__conditions]:
            for param in condition_parameters:
                parameters.append(param)

        return parameters

    def build(self) -> str:
        set_string = ", ".join([f"`{item.column}` = %s" for item in self.__updates])

        condition_string = ""
        for condition in self.__conditions:
            condition_sql = condition._condition
            condition_type = condition._type
            condition_string += f" {condition_type} ({condition_sql})"

        return f"update `{self.__table_name}` set {set_string}{condition_string}".strip()

class FirstUpdateStep(Generic[TableDefinitionType]):
    
    __query_builder: UpdateQueryBuilder

    def __init__(self, query_builder: UpdateQueryBuilder):
        super().__init__()
        self.__query_builder = query_builder

    def set(self, column: ColumnDefinition[TableDefinitionType, ParameterType], value: ParameterType) -> UpdateStep[TableDefinitionType]:
        self.__query_builder.add_update(Update(column.column_name, value))
        return UpdateStep(self.__query_builder)

class UpdateStep(Generic[TableDefinitionType]):
    
    __query_builder: UpdateQueryBuilder

    def __init__(self, query_builder: UpdateQueryBuilder):
        super().__init__()
        self.__query_builder = query_builder

    def set(self, column: ColumnDefinition[TableDefinitionType, ParameterType], value: ParameterType) -> UpdateStep[TableDefinitionType]:
        self.__query_builder.add_update(Update(column.column_name, value))
        return UpdateStep(self.__query_builder)

    def where(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[TableDefinitionType]:
        condition._type = "where"
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)
    
    def execute(self):
        sql_query = self.__query_builder.build()
        parameters = self.__query_builder.get_parameters()

        sql.execute(sql_query, parameters)

class WhereStep(Generic[TableDefinitionType]):
    
    __query_builder: UpdateQueryBuilder

    def __init__(self, query_builder: UpdateQueryBuilder):
        super().__init__()
        self.__query_builder = query_builder

    def and_(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[TableDefinitionType]:
        condition._type = "and"
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def or_(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[TableDefinitionType]:
        condition._type = "or"
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def execute(self):
        sql_query = self.__query_builder.build()
        parameters = self.__query_builder.get_parameters()

        sql.execute(sql_query, parameters)

def update(table: TableDefinition[Any, TableDefinitionType]) -> FirstUpdateStep[TableDefinitionType]:
    return FirstUpdateStep(UpdateQueryBuilder(table.table_name))

from __future__ import annotations
from typing import TypeVar, Generic, Any, Type
import devkit.sql as sql

ModelType = TypeVar("ModelType", bound=sql.Model)
TableDefinitionType = TypeVar("TableDefinitionType", bound="TableDefinition[Any, Any]")
ParameterType = TypeVar("ParameterType")

class Condition(Generic[TableDefinitionType, ParameterType]):

    _type: str
    _condition: str
    _parameters: list[Any]

    def __init__(self, condition: str, parameters: list[Any]) -> None:
        super().__init__()
        self._type = ""
        self._condition = condition
        self._parameters = parameters

class ColumnDefinition(Generic[TableDefinitionType, ParameterType]):
    
    column_name: str

    def __init__(self, column_name: str) -> None:
        super().__init__()
        self.column_name = column_name

    def eq(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"`{self.column_name}` = ?", [other])
    
    def lt(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"`{self.column_name}` < ?", [other])

    def le(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"`{self.column_name}` <= ?", [other])
    
    def gt(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"`{self.column_name}` > ?", [other])
    
    def ge(self, other: ParameterType) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"`{self.column_name}` >= ?", [other])
    
    def in_(self, other: list[ParameterType]) -> Condition[TableDefinitionType, ParameterType]:
        wildcard_parameters = ", ".join(["?" for _ in other])
        return Condition(f"`{self.column_name}` in ({wildcard_parameters})", other)

class NullableColumnDefinition(ColumnDefinition[TableDefinitionType, ParameterType]):

    def is_null(self) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"`{self.column_name}` is null", [])

    def is_not_null(self) -> Condition[TableDefinitionType, ParameterType]:
        return Condition(f"`{self.column_name}` is not null", [])

class TableDefinition(Generic[ModelType, TableDefinitionType]):
    
    table_name: str
    table_type: Type[ModelType]

    def __init__(self, table_name: str, table_type: Type[ModelType]) -> None:
        super().__init__()
        self.table_name = table_name
        self.table_type = table_type
from __future__ import annotations
from devkit.sql.query.definitions import TableDefinition, Condition, ModelType, TableDefinitionType
from typing import Generic, Any, Type
import devkit.sql as sql

class SelectQueryBuilder:
    
    __table_name: str
    __table_type: Type[Any]
    __conditions: list[Condition[Any, Any]]
    __limit: int | None

    def __init__(self, table_name: str, table_type: Type[Any]) -> None:
        self.__table_name = table_name
        self.__table_type = table_type
        self.__conditions = []
        self.__limit = None

    def add_condition(self, condition: Condition[Any, Any]):
        self.__conditions.append(condition)

    def set_limit(self, limit: int):
        self.__limit = limit

    def get_parameters(self) -> list[Any]:
        parameters: list[Any] = []

        for condition_parameters in [item._parameters for item in self.__conditions]:
            for param in condition_parameters:
                parameters.append(param)

        return parameters

    def build(self) -> str:
        condition_string = ""
        for condition in self.__conditions:
            condition_sql = condition._condition
            condition_type = condition._type
            condition_string += f" {condition_type} ({condition_sql})"

        limit_string = ""
        if self.__limit != None:
            limit_string = f" limit {self.__limit}"

        return f"select * from `{self.__table_name}`{condition_string}{limit_string}".strip()
    
    def get_table_type(self) -> Type[Any]:
        return self.__table_type

class SelectFromStep(Generic[ModelType, TableDefinitionType]):
    
    __query_builder: SelectQueryBuilder

    def __init__(self, query_builder: SelectQueryBuilder) -> None:
        super().__init__()
        self.__query_builder = query_builder

    def where(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[ModelType, TableDefinitionType]:
        condition._type = "where"
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def limit(self, limit: int) -> LimitStep[ModelType, TableDefinitionType]:
        self.__query_builder.set_limit(limit)
        return LimitStep(self.__query_builder)

    def fetch(self) -> list[ModelType]:
        sql_query = self.__query_builder.build()
        parameters = self.__query_builder.get_parameters()

        return sql.fetch_as(sql_query, self.__query_builder.get_table_type(), parameters)

    def fetch_one(self) -> ModelType | None:
        result = self.limit(1).fetch()

        if len(result) == 0: return None
        return result[0]

class WhereStep(Generic[ModelType, TableDefinitionType]):

    __query_builder: SelectQueryBuilder

    def __init__(self, query_builder: SelectQueryBuilder) -> None:
        super().__init__()
        self.__query_builder = query_builder

    def and_(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[ModelType, TableDefinitionType]:
        condition._type = "and"
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def or_(self, condition: Condition[TableDefinitionType, Any]) -> WhereStep[ModelType, TableDefinitionType]:
        condition._type = "or"
        self.__query_builder.add_condition(condition)
        return WhereStep(self.__query_builder)

    def limit(self, limit: int) -> LimitStep[ModelType, TableDefinitionType]:
        self.__query_builder.set_limit(limit)
        return LimitStep(self.__query_builder)

    def fetch(self) -> list[ModelType]:
        sql_query = self.__query_builder.build()
        parameters = self.__query_builder.get_parameters()

        return sql.fetch_as(sql_query, self.__query_builder.get_table_type(), parameters)

    def fetch_one(self) -> ModelType | None:
        result = self.limit(1).fetch()

        if len(result) == 0: return None
        return result[0]

class LimitStep(Generic[ModelType, TableDefinitionType]):
    
    __query_builder: SelectQueryBuilder

    def __init__(self, query_builder: SelectQueryBuilder) -> None:
        super().__init__()
        self.__query_builder = query_builder

    def fetch(self) -> list[ModelType]:
        sql_query = self.__query_builder.build()
        parameters = self.__query_builder.get_parameters()

        return sql.fetch_as(sql_query, self.__query_builder.get_table_type(), parameters)

def select(table: TableDefinition[ModelType, TableDefinitionType]) -> SelectFromStep[ModelType, TableDefinitionType]:
    return SelectFromStep(SelectQueryBuilder(table.table_name, table.table_type))

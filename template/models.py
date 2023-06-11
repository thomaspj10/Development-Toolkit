from __future__ import annotations

from dataclasses import dataclass, field
from devkit.sql import Model, fetch_as
from devkit.sql.query.definitions import ColumnDefinition, TableDefinition

@dataclass(slots=True)
class DevkitMigrations(Model):
    id: int = field(init=False, default=None) # type: ignore
    file: str
    executed_successfully: bool

    @staticmethod
    def find_by_id(id: int) -> DevkitMigrations | None:
        result = fetch_as(f"select rowid as id, * from `DevkitMigrations` where `rowid` = ?", DevkitMigrations, [id])
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[DevkitMigrations]:
        return fetch_as(f"select rowid as id, * from `DevkitMigrations`", DevkitMigrations)


class DevkitMigrationsTable(TableDefinition[DevkitMigrations, 'DevkitMigrationsTable']):
    ID: ColumnDefinition[DevkitMigrationsTable, int] = ColumnDefinition('id')
    FILE: ColumnDefinition[DevkitMigrationsTable, str] = ColumnDefinition('file')
    EXECUTED_SUCCESSFULLY: ColumnDefinition[DevkitMigrationsTable, bool] = ColumnDefinition('executed_successfully')

DEVKIT_MIGRATIONS = DevkitMigrationsTable('DevkitMigrations', DevkitMigrations)


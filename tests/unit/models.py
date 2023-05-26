from __future__ import annotations

from dataclasses import dataclass, field
from devkit.sql import Model, fetch_as
from devkit.sql.query.definitions import ColumnDefinition, TableDefinition

@dataclass(slots=True)
class Address(Model):
    id: int = field(init=False, default=None) # type: ignore
    name: str | None

    @staticmethod
    def find_by_id(id: int) -> Address | None:
        result = fetch_as(f"select rowid as id, * from `Address` where `rowid` = ?", Address, [id])
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[Address]:
        return fetch_as(f"select rowid as id, * from `Address`", Address)


class AddressTable(TableDefinition[Address, 'AddressTable']):
    ID: ColumnDefinition[AddressTable, int] = ColumnDefinition('id')
    NAME: ColumnDefinition[AddressTable, str] = ColumnDefinition('name')

ADDRESS = AddressTable('Address', Address)


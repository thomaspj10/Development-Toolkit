from __future__ import annotations

from dataclasses import dataclass, field
from devkit.sql import Model, fetch_as

@dataclass(slots=True)
class Address(Model):
    id: int = field(init=False, default=None) # type: ignore
    name: str | None

    @staticmethod
    def find_by_id(id: int) -> Address | None:
        result = fetch_as(f"select rowid as id, * from `Address` where `rowid` = {id}", Address)
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[Address]:
        return fetch_as(f"select rowid as id, * from `Address`", Address)



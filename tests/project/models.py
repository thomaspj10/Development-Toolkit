from __future__ import annotations

from dataclasses import dataclass, field
from devkit.sql import Model, fetch_as
from typing import Self

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


@dataclass(slots=True)
class User(Model):
    id: int = field(init=False, default=None) # type: ignore
    name: str
    address_id: int | None

    @staticmethod
    def find_by_id(id: int) -> User | None:
        result = fetch_as(f"select rowid as id, * from `User` where `rowid` = {id}", User)
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[User]:
        return fetch_as(f"select rowid as id, * from `User`", User)

    def get_address(self: Self) -> Address | None:
        if self.address_id == None: 
            return None
        
        return Address.find_by_id(self.address_id)



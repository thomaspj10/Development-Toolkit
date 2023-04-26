from __future__ import annotations

from dataclasses import dataclass, field
from devkit.sql import Model, fetch_as

@dataclass(slots=True)
class Address(Model):
    id: int = field(init=False, default=None) # type: ignore
    name: str | None

    @staticmethod
    def find_by_id(id: int) -> Address | None:
        result = fetch_as(f"select * from `Address` where `id` = {id}", Address)
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[Address]:
        return fetch_as(f"select * from `Address`", Address)


@dataclass(slots=True)
class User(Model):
    id: int = field(init=False, default=None) # type: ignore
    name: str | None
    address_id: int | None

    @staticmethod
    def find_by_id(id: int) -> User | None:
        result = fetch_as(f"select * from `User` where `id` = {id}", User)
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[User]:
        return fetch_as(f"select * from `User`", User)



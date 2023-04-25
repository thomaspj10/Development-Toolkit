from __future__ import annotations

from dataclasses import dataclass, field
from devkit.sql import Model, fetch_as
from typing import Self

@dataclass(slots=True)
class User(Model):
    id: int = field(init=False, default=None) # type: ignore
    name: str
    address_id: int

    @staticmethod
    def find_by_id(id: int) -> User | None:
        result = fetch_as(f"select * from `User` where `id` = {id}", User)
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[User]:
        return fetch_as(f"select * from `User`", User)

    def get_address(self: Self) -> Address:
        return Address.find_by_id(self.address_id) # type: ignore


@dataclass(slots=True)
class Address(Model):
    id: int = field(init=False, default=None) # type: ignore
    name: str

    @staticmethod
    def find_by_id(id: int) -> Address | None:
        result = fetch_as(f"select * from `Address` where `id` = {id}", Address)
        
        if len(result) == 0:
            return None
                
        return result[0]

    @staticmethod
    def find_all() -> list[Address]:
        return fetch_as(f"select * from `Address`", Address)



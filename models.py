from __future__ import annotations

from dataclasses import dataclass, field
from sql import fetch_as, Model

@dataclass(slots=True)
class User(Model):
    id: int | None = field(init=False, default=None)
    name: str

    @staticmethod
    def find_by_id(id: int) -> User | None:
        result = fetch_as(f"select * from `User` where `id` = {id}", User)
        
        if len(result) == 0:
            return None
                
        return result[0]
        
    @staticmethod
    def find_all() -> list[User]:
        return fetch_as(f"select * from `User`", User)


from __future__ import annotations
import sql.database as db
from dataclasses import dataclass, field

@dataclass(slots=True)
class User(db.Model):
    id: int | None = field(init=False, default=None)
    name: str
    
    @staticmethod
    def find_by_id(id: int) -> User | None:
        result = db.fetch_as(f"select * from `User` where `id` = {id}", User)
        
        if len(result) == 0:
            return None
        
        return result[0]
    
    @staticmethod
    def find_all() -> list[User]:
        return db.fetch_as(f"select * from `User`", User)

# user = User("Bas")
# print(user)
# user.store()

print(User.find_by_id(6))

for user in User.find_all():
    print(user)

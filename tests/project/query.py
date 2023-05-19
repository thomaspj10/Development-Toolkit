from __future__ import annotations
import models
from devkit.sql.querying import TableDefinition, ColumnDefinition

class UserTable(TableDefinition[models.User, "UserTable"]):
    ID: ColumnDefinition[UserTable, int] = ColumnDefinition("id")
    NAME: ColumnDefinition[UserTable, str] = ColumnDefinition("name")

USER = UserTable("User", models.User)

class AddressTable(TableDefinition[models.Address, "AddressTable"]):
    ID: ColumnDefinition[AddressTable, int] = ColumnDefinition("id")
    NAME: ColumnDefinition[AddressTable, str] = ColumnDefinition("name")

ADDRESS = AddressTable("Address", models.Address)

import devkit.sql as sql

sql.set_sqlite_file("database.db")
sql.set_debug(True)

result = sql.selectFrom(USER).where(USER.ID.eq(1)).or_(USER.NAME.eq("Aap")).fetch()
print(result)

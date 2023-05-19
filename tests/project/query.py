import devkit.sql as sql
from models import USER

sql.set_sqlite_file("database.db")
sql.set_debug(True)

result = sql.selectFrom(USER).where(USER.ID.eq(1)).or_(USER.NAME.eq("Aap")).fetch()
print(result)

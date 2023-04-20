import sql
import models

sql.set_sqlite_file("database.db")

# sql.execute("drop table User")
# sql.execute("create table User (id integer primary key autoincrement, name varchar(255))")

# user = User("Bas")
# print(user)
# user.store()

print(models.User.find_by_id(6))

for user in models.User.find_all():
    print(user)

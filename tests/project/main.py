import devkit.sql as sql
import models

sql.set_sqlite_file("database.db")

# sql.execute("drop table User")
# sql.execute("drop table Address")
# sql.execute("create table Address (id integer primary key autoincrement, name varchar(255))")
# sql.execute("create table User (id integer primary key autoincrement, name varchar(255), address_id int, foreign key (address_id) references User(id))")

# address = models.Address("Straat")
# address.store()

# user = models.User("Aap", address.id)
# user.store()
# print(user)

for user in models.User.find_all():
    address = user.get_address()
    print(user)
    print(address)

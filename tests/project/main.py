import devkit.sql as sql
import models

sql.set_sqlite_file("database.db")

sql.execute("drop table User")
sql.execute("drop table Address")
sql.execute("create table Address (id integer primary key autoincrement, name varchar(255))")
sql.execute("create table User (id integer primary key autoincrement, name varchar(255) not null, address_id int not null, foreign key (address_id) references Address(id))")

sql.generate_models()

address = models.Address("Straat")

user = models.User("Aap", address.id)
user.store()

for user in models.User.find_all():
    address = user.get_address()
    print(user)
    print(address)

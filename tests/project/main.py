import devkit.sql as sql
import models

sql.set_sqlite_file("database.db")
sql.set_debug(True)

def start():
    sql.execute("drop table if exists User")
    sql.execute("drop table if exists Address")
    sql.execute("create table Address (id integer primary key autoincrement, name varchar(255))")
    sql.execute("create table User (id integer primary key autoincrement, name varchar(255) not null, address_id int, foreign key (address_id) references Address(id))")
    # sql.execute("insert into User values (?, ?, ?)", [None, "Thomas", None])

    address = models.Address("Straat")

    user = models.User("Aap", address.id)

    for user in models.User.find_all():
        address = user.get_address()
        print(user)
        print(address)

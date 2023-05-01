# Development Toolkit
Development toolkit to increase velocity and code quality.

![Tests](https://github.com/thomaspj10/Development-Toolkit/actions/workflows/tests.yaml/badge.svg)

## Installation
1. Go into the base directory.
2. `pip install -e .`

## Test suite
1. Run the test suite `python -m unittest`

## Examples

This will require two runs, because the models have not been generated yet.

```py
import devkit.sql as sql
import models

sql.set_sqlite_file("database.db")
sql.set_debug(True)

sql.execute("drop table User")
sql.execute("drop table Address")
sql.execute("create table Address (id integer primary key autoincrement, name varchar(255))")
sql.execute("create table User (id integer primary key autoincrement, name varchar(255) not null, address_id int, foreign key (address_id) references Address(id))")

sql.generate_models()

address = models.Address("Straat")

user = models.User("Aap", address.id)

for user in models.User.find_all():
    address = user.get_address()
    print(user)
    print(address)
```

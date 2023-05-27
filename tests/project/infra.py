import devkit.infra as infra

from sanic import Sanic
from sanic.worker.loader import AppLoader

def run_migrations():
    import devkit.sql as sql
    sql.set_sqlite_file("database.db")

    sql.migrate()

def generate_models():
    import devkit.sql as sql
    sql.set_sqlite_file("database.db")

    sql.execute("create table if not exists Address (id integer primary key autoincrement, name varchar(255))")
    sql.execute("create table if not exists User (id integer primary key autoincrement, name varchar(255) not null, address_id int, verified boolean, foreign key (address_id) references Address(id))")

    sql.generate_models()

def start():
    import main
    loader = AppLoader(factory=main.start)
    app = loader.load()
    app.prepare(port=9999) # type: ignore
    Sanic.serve(primary=app, app_loader=loader)

if __name__ == "__main__":
    with infra.define() as definition:
        definition.task("start", [generate_models, start])

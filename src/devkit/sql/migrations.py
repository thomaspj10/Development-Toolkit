import os
import glob
import devkit.sql as sql
import devkit.sql.database as database
import devkit.logger as logger
import time
import secrets

def current_milli_time():
    return round(time.time() * 1000)

def find_all_migrations():
    return glob.glob("./migrations/*.sql")

def run_migrations():
    """
    Run all migrations which have not been run yet.
    """

    for migration_path in find_all_migrations():
        file = os.path.basename(migration_path)

        migrations_row = database.fetch("select * from DevkitMigrations where `file` = ?", [file])

        success = False
        if len(migrations_row) == 0:
            database.insert("insert into DevkitMigrations values(?, ?, ?)", [None, file, False])
        else:
            success = migrations_row[0]["executed_successfully"] == 1
        
        if success:
            logger.info(f"Ignoring migration {file}")
        else:
            logger.info(f"Running migration {file}")
            run_migration(file)

def run_migration(file: str):
    with open(os.path.join("migrations", file), "r") as f:
        success = False

        try:
            sql = "BEGIN;\n\n" + f.read() + "\n\nCOMMIT;"
            database.execute_script(sql)
            success = True
        except Exception as e:
            database.execute("ROLLBACK;")
            logger.error(f"There was an error while trying to execute migration {file}")
            logger.error(e)

        database.execute("update DevkitMigrations set `executed_successfully` = ? where file = ?", [success, file])

def create_migration():
    """
    Create a new migration.
    """
    file_name = f"migration__{current_milli_time()}__{secrets.token_hex(1)}"

    with open(f"./migrations/{file_name}.sql", "w") as f:
        f.write("")

def setup():
    """
    Setup the structure required for migrations.
    """

    os.makedirs("migrations", exist_ok=True)

    sql.execute("create table if not exists DevkitMigrations (id integer primary key autoincrement not null, file varchar(255) not null, executed_successfully boolean not null)")

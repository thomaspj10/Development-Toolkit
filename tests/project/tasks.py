import devkit.tasks as tasks

def generate_models():
    import devkit.sql as sql
    sql.set_sqlite_file("database.db")
    sql.generate_models()

def start():
    import main
    main.start()

tasks.define("start", [generate_models, start])

if __name__ == "__main__":
    tasks.start()

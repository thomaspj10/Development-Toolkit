import devkit.tasks as tasks
import devkit.sql as sql
import os

@tasks.task
def generate_models():
    sql.set_sqlite_file("database.db")
    sql.generate_models()

@tasks.task
def start():
    os.system("python main.py")

tasks.initialize([generate_models, start])

from typing import Callable
import sys
from contextlib import contextmanager
from dataclasses import dataclass
import devkit.sql.migrations
import devkit.sql as sql
import os

CALLABLE_TYPE = Callable[..., None]

@dataclass
class Task:
    name: str
    description: str
    functions: list[CALLABLE_TYPE]
    is_database_required: bool

class InfraDefinition:
    
    _tasks: list[Task]
    
    _host: str
    _port: int
    _database: str
    _user: str
    _password: str

    def __init__(self) -> None:
        self._tasks = []

    def task(self, name: str, description: str, functions: list[CALLABLE_TYPE], is_database_required: bool = False):
        """
        Define a new task which can be dynamically invoked from the cli.
        """
        self._tasks.append(Task(name, description, functions, is_database_required))


    def command(self, name: str, description: str, commands: list[str], is_database_required: bool = False):
        """
        Define a new task which will act as an alias for shell commands.
        """
        def wrapper():
            for command in commands:
                os.system(command)
        
        self._tasks.append(Task(name, description, [wrapper], is_database_required))

    def use_database(self, host: str, port: int, database: str, user: str, password: str):
        """
        Automatically connect to the database. Creates two _tasks for the creation and running of migrations.
        """
        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password

        self.task("run_migrations", "Run all migrations which have not run yet.", [devkit.sql.migrations.run_migrations])
        self.task("create_migration", "Create a new migration.", [devkit.sql.migrations.create_migration])

def print_help(definition: InfraDefinition):
    print("Available _tasks:")
    for index, task in enumerate(definition._tasks):
        print(f"{index + 1}. {task.name.ljust(20)} - {task.description}")

@contextmanager
def define(__name__: str):
    """
    The global variable `__name__` must be passed as an argument.
    """
    definition = InfraDefinition()
    yield definition

    if __name__ != "__main__":
        return

    arguments = sys.argv[1::]

    if len(arguments) == 0:
        print_help(definition)
        return
    
    if arguments[0] not in [item.name for item in definition._tasks]:
        print_help(definition)
        return
    
    task = [item for item in definition._tasks if item.name == arguments[0]][0]

    if task.is_database_required:
        sql.connect(definition._host, definition._port, definition._database, definition._user, definition._password)

    for func in task.functions:
        func()

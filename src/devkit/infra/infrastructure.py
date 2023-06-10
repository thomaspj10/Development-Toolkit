from typing import Callable
import sys
from contextlib import contextmanager
from multiprocessing import Process
from dataclasses import dataclass
import devkit.sql.migrations
import os

CALLABLE_TYPE = Callable[..., None]

@dataclass
class Task:
    name: str
    description: str
    functions: list[CALLABLE_TYPE]

class InfraDefinition:
    
    tasks: list[Task]

    def __init__(self) -> None:
        self.tasks = []

    def task(self, name: str, description: str, functions: list[CALLABLE_TYPE]):
        """
        Define a new task which can be dynamically invoked from the cli.
        """
        self.tasks.append(Task(name, description, functions))


    def command(self, name: str, description: str, command: str):
        """
        Define a new task which will act as an alias for a command.
        """
        def wrapper():
            os.system(command)
        
        self.tasks.append(Task(name, description, [wrapper]))

    def use_migrations(self):
        """
        Automatically create two tasks for the creation and running of migrations.
        """
        devkit.sql.migrations.setup()

        self.task("run_migrations", "Run all migrations which have not run yet.", [devkit.sql.migrations.run_migrations])
        self.task("create_migration", "Create a new migration.", [devkit.sql.migrations.create_migration])

def print_help(definition: InfraDefinition):
    print("Available tasks:")
    for index, task in enumerate(definition.tasks):
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
    
    if arguments[0] not in [item.name for item in definition.tasks]:
        print_help(definition)
        return
    
    task = [item for item in definition.tasks if item.name == arguments[0]][0]

    for func in task.functions:
        process = Process(target=func)
        process.start()
        process.join()

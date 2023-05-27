from typing import Callable
import sys
from contextlib import contextmanager
from multiprocessing import Process

CALLABLE_TYPE = Callable[..., None]

class InfraDefinition:
    
    tasks: dict[str, list[CALLABLE_TYPE]]

    def __init__(self) -> None:
        self.tasks = {}

    """
    Define a new task which can be dynamically invoked from the cli.
    """
    def task(self, name: str, functions: list[CALLABLE_TYPE]):
        self.tasks[name] = functions

def __print_help(definition: InfraDefinition):
    print("Available tasks:")
    for task in definition.tasks:
        print(f"- {task}")

@contextmanager
def define():
    definition = InfraDefinition()
    yield definition

    arguments = sys.argv[1::]

    if len(arguments) == 0:
        __print_help(definition)
        return
    
    if arguments[0] not in definition.tasks:
        __print_help(definition)
        return
    
    for func in definition.tasks[arguments[0]]:
        process = Process(target=func)
        process.start()
        process.join()

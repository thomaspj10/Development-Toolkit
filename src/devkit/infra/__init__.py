from typing import Callable
import sys
from multiprocessing import Process

CALLABLE_TYPE = Callable[..., None]

__tasks: dict[str, list[CALLABLE_TYPE]] = {}

def __print_help():
    print("Available tasks:")
    for task in __tasks:
        print(f"- {task}")

def start():
    arguments = sys.argv[1::]

    if len(arguments) == 0:
        __print_help()
        return
    
    if arguments[0] not in __tasks:
        __print_help()
        return
    
    for func in __tasks[arguments[0]]:
        process = Process(target=func)
        process.start()
        process.join()

"""
Define a new task which can be dynamically invoked from the cli.
"""
def define_task(name: str, functions: list[CALLABLE_TYPE]):
    __tasks[name] = functions

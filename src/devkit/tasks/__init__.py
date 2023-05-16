from typing import Callable

CALLABLE_TYPE = Callable[..., None]

class Task:

    __name: str
    __func: CALLABLE_TYPE

    def __init__(self, name: str, func: CALLABLE_TYPE) -> None:
        self.__name = name
        self.__func = func

    def call(self):
        print(f"[TASK] - {self.__name}")
        self.__func()

def initialize(tasks: list[Task]):
    for task in tasks:
        task.call()

def task(func: CALLABLE_TYPE) -> Task:
    return Task(func.__name__, func)

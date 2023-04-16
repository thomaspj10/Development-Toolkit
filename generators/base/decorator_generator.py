from dataclasses import dataclass
from generators.igenerator import IGenerator

@dataclass
class DecoratorArgument:
    name: str
    value: str
     
class DecoratorGenerator(IGenerator):
    
    __decorator: str
    __arguments: list[DecoratorArgument]
    
    def __init__(self) -> None:
        self.__arguments = []
        
    def set_decorator(self, decorator: str):
        self.__decorator = decorator
        
    def add_argument(self, name: str, value: str):
        self.__arguments.append(DecoratorArgument(name, value))
        
    def generate(self, indent: int) -> str:
        result = ""
        
        arguments_result = ""
        if len(self.__arguments) != 0:
            arguments_result = "(" + ", ".join([f"{arg.name}={arg.value}" for arg in self.__arguments]) + ")"
        
        result += f"@{self.__decorator}{arguments_result}"
        
        return result
from dataclasses import dataclass
from devkit.generators.base.decorator_generator import DecoratorGenerator
from devkit.generators.igenerator import IGenerator

INDENT = " " * 4

@dataclass
class FunctionArgument:
    name: str
    type: str

class FunctionGenerator(IGenerator):
    
    __name: str
    __return_type: str
    __is_async: bool
    __body: str
    __arguments: list[FunctionArgument]
    __decorators: list[DecoratorGenerator]
    
    def __init__(self) -> None:
        super().__init__()
        self.__arguments = []
        self.__decorators = []
        self.__return_type = "None"
        self.__is_async = False
        
    def set_name(self, name: str):
        self.__name = name
        
    def set_return_type(self, return_type: str):
        self.__return_type = return_type
        
    def set_body(self, body: str):
        self.__body = body
        
    def add_argument(self, name: str, type: str):
        self.__arguments.append(FunctionArgument(name, type))
        
    def add_decorator(self, decorator: DecoratorGenerator):
        self.__decorators.append(decorator)
        
    def set_is_async(self, is_async: bool):
        self.__is_async = is_async
        
    def generate(self, indent: int) -> str:
        result = ""
    
        for decorator in self.__decorators:
            result += f"{INDENT * indent}{decorator.generate(indent)}\n"
            
        arguments = ", ".join(f"{argument.name}: {argument.type}" for argument in self.__arguments)
        async_result = "async " if self.__is_async else ""
        result += f"{INDENT * indent}{async_result}def {self.__name}({arguments}) -> {self.__return_type}:\n"
        
        for line in self.__body.split("\n"):
            result += f"{INDENT * (indent + 1)}{line}\n"
        
        return result

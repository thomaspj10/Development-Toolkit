from dataclasses import dataclass
from devkit.generators.igenerator import IGenerator
from devkit.generators.base.function_generator import FunctionGenerator
from devkit.generators.base.decorator_generator import DecoratorGenerator

INDENT = " " * 4

@dataclass
class ClassAttribute:
    name: str
    type: str
    default_value: str | None

class ClassGenerator(IGenerator):
    
    __name: str
    __decorators: list[DecoratorGenerator]
    __inherited_classes: list[str]
    __attributes: list[ClassAttribute]
    __functions: list[FunctionGenerator]
    
    def __init__(self) -> None:
        super().__init__()
        self.__decorators = []
        self.__inherited_classes = []
        self.__attributes = []
        self.__functions = []
    
    def set_name(self, name: str):
        self.__name = name
        
    def add_decorator(self, decorator: DecoratorGenerator):
        self.__decorators.append(decorator)
        
    def add_inherited_class(self, class_name: str):
        self.__inherited_classes.append(class_name)

    def add_attribute(self, name: str, type: str, default_value: str | None = None):
        self.__attributes.append(ClassAttribute(name, type, default_value))

    def add_function(self, function_generator: FunctionGenerator):
        self.__functions.append(function_generator)

    def generate(self, indent: int) -> str:
        result = ""
        
        # Decorators
        for decorator in self.__decorators:
            result += decorator.generate(0) + "\n"
        
        # The class with optional inheritance
        inherited_classes_result = ""
        if len(self.__inherited_classes) != 0:
            inherited_classes_result = "(" + ", ".join(self.__inherited_classes) + ")"
        
        result += f"class {self.__name}{inherited_classes_result}:\n"
        
        # The class attributes
        for attribute in self.__attributes:
            default_value_string = ""
            if attribute.default_value != None:
                default_value_string = f" = {attribute.default_value}"
            result += f"{INDENT}{attribute.name}: {attribute.type}{default_value_string}\n"
        
        # The class functions
        if len(self.__functions) > 0:
            result += "\n"
        
        for function in self.__functions:
            result += function.generate(1) + "\n"
        
        if len(self.__attributes) == 0 and len(self.__functions) == 0:
            result += f"{INDENT}pass\n\n"

        return result

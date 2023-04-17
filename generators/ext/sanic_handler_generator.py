from generators.igenerator import IGenerator
from typing import Literal
from generators.base import FunctionGenerator, DecoratorGenerator

class SanicHandlerGenerator(IGenerator):
    
    __method: str
    __name: str
    __body: str
    __route: str
    __params_class: str | None
    __params_type: str
    
    def __init__(self) -> None:
        super().__init__()
        self.__method = "get"
        self.__params_class = None
    
    def set_method(self, method: Literal["get", "post"]):
        self.__method = method
    
    def set_route_name(self, name: str):
        self.__name = name
        
    def set_body(self, body: str):
        self.__body = body
    
    def set_route(self, route: str):
        self.__route = route
    
    def set_params_class(self, params_class: str, type: Literal["query", "json", "form"]):
        self.__params_class = params_class
        self.__params_type = type
    
    def generate(self, indent: int) -> str:
        method_decorator = DecoratorGenerator()
        method_decorator.add_argument("uri", f'"{self.__route}"')
        method_decorator.set_decorator(f"app.{self.__method}")
        
        function_generator = FunctionGenerator()
        function_generator.set_name(self.__name)
        function_generator.set_body(self.__body)
        function_generator.set_return_type("HTTPResponse")
        function_generator.add_argument("request", "Request")
        function_generator.set_is_async(True)
        function_generator.add_decorator(method_decorator)
        
        if self.__params_class != None:
            validation_decorator = DecoratorGenerator()
            validation_decorator.set_decorator("validate")
            validation_decorator.add_argument(self.__params_type, self.__params_class)
            function_generator.add_decorator(validation_decorator)
            
            argument_name = "query" if self.__params_type == "query" else "body"
            function_generator.add_argument(argument_name, self.__params_class)
            
            self.add_from_import("sanic_ext", ["validate"])
        
        self.add_from_import("sanic.response", ["HTTPResponse"])
        self.add_from_import("sanic.request", ["Request"])
        
        return function_generator.generate(indent)
    
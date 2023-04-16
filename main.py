# from generators.base import ClassGenerator, FunctionGenerator, DecoratorGenerator

# cls = ClassGenerator()
# cls.set_name("MyClass")
# cls.add_inherited_class("InheritedClass")
# cls.add_attribute("age", "int")

# decorator = DecoratorGenerator()
# decorator.set_decorator("dataclass")
# cls.add_decorator(decorator)

# func = FunctionGenerator()
# func.set_name("test_function")
# func.add_argument("age", "int")
# func.add_argument("name", "str")
# func.set_body("print(age, name)")

# cls.add_function(func)

# print(cls.generate(0))

from generators.ext.sanic_handler_generator import SanicHandlerGenerator

handler = SanicHandlerGenerator()
handler.set_body("...")
handler.set_method("get")
handler.set_route("/")
handler.set_route_name("homepage")
handler.set_params_class("HomepageParams", "form")

print(handler.generate(0))

from generators.ext import SanicHandlerGenerator
from generators.base import ClassGenerator, RawCodeGenerator, DecoratorGenerator
from python_file import python_file

with python_file("test.py") as pf:
    raw = RawCodeGenerator()
    raw.set_code("""app = Sanic("test")

if __name__ == "__main__":
    app.run("localhost", 5000)
""")
    
    raw.add_from_import("sanic", ["Sanic"])
        
    dataclass_decorator = DecoratorGenerator()
    dataclass_decorator.set_decorator("dataclass")
    dataclass_decorator.add_from_import("dataclasses", ["dataclass"])
    
    homepage_params_cls = ClassGenerator()
    homepage_params_cls.set_name("HomepageParams")
    homepage_params_cls.add_decorator(dataclass_decorator)
    homepage_params_cls.add_attribute("name", "str")
    
    handler = SanicHandlerGenerator()
    handler.set_body("return text('hello!')")
    handler.set_method("get")
    handler.set_route("/")
    handler.set_route_name("homepage")
    handler.set_params_class("HomepageParams", "query")
    
    handler.add_from_import("sanic", ["text"])

    pf.add_generator(raw)
    pf.add_generator(homepage_params_cls)
    pf.add_generator(handler)

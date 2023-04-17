from generators.ext import SanicHandlerGenerator
from python_file import python_file

from generators.base import RawCodeGenerator

with python_file("test.py") as pf:
    raw = RawCodeGenerator()
    raw.set_code("""app = Sanic("test")

if __name__ == "__main__":
    app.run("localhost", 5000)

@dataclass
class HomepageParams:
    name: str
    """)
    
    raw.add_from_import("sanic", ["Sanic"])
    raw.add_from_import("dataclasses", ["dataclass"])
        
    handler = SanicHandlerGenerator()
    handler.set_body("return text('hello!')")
    handler.set_method("get")
    handler.set_route("/")
    handler.set_route_name("homepage")
    handler.set_params_class("HomepageParams", "query")
    
    handler.add_from_import("sanic", ["text"])

    pf.add_generator(raw)
    pf.add_generator(handler)

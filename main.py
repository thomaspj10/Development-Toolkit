from generators.ext import SanicHandlerGenerator
from python_file import python_file

with python_file("test.py") as pf:
    handler = SanicHandlerGenerator()
    handler.set_body("...")
    handler.set_method("get")
    handler.set_route("/")
    handler.set_route_name("homepage")
    handler.set_params_class("HomepageParams", "form")

    pf.add_generator(handler)

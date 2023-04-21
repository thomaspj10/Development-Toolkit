from contextlib import contextmanager
from python_file import PythonFile, generate
from typing import Any
from generators.base import DecoratorGenerator, ClassGenerator, RawCodeGenerator
from generators.ext import SanicHandlerGenerator

class TestResult:
    name: str
    passing: bool

    def __init__(self, name: str) -> None:
        self.name = name
        self.passing = True
        
    def assert_equals(self, value: Any, other: Any):
        self.passing = value == other

results: list[TestResult] = []

@contextmanager
def test(name: str):
    test_result = TestResult(name)
    results.append(test_result)
    
    yield test_result

with test("Sanic handler") as test_result:
    pf = PythonFile()
        
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

    required_result = """from sanic import HTTPResponse, Request, Sanic, text
from dataclasses import dataclass
from sanic_ext import validate

app = Sanic("test")

if __name__ == "__main__":
app.run("localhost", 5000)

@dataclass
class HomepageParams:
    name: str

@app.get(uri="/")
@validate(query=HomepageParams)
async def homepage(request: Request, query: HomepageParams) -> HTTPResponse:
    return text('hello!')

"""
    
    test_result.assert_equals(generate(pf), required_result)



total_count = len(results)
passing_count = len([result for result in results if result.passing])

print(f"Passing: {passing_count} / {total_count}")

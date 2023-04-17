from sanic import text, Sanic
from dataclasses import dataclass
from sanic_ext import validate
from sanic.response import HTTPResponse
from sanic.request import Request

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


from sanic.response import HTTPResponse
from sanic.request import Request
from sanic import Sanic
from sanic_ext import validate
from dataclasses import dataclass


app = Sanic()

@dataclass
class HomepageParams:
    name: str

@app.get(uri="/")
@validate(form=HomepageParams)
async def homepage(request: Request, body: HomepageParams) -> HTTPResponse:
    ...
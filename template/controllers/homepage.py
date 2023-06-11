from sanic import Blueprint, Request, HTTPResponse, html
import views.homepage

bp = Blueprint("homepage")

@bp.get("/")
async def homepage(request: Request) -> HTTPResponse:
    return html(str(
        views.homepage.homepage("Welcome to my site!")
    ))

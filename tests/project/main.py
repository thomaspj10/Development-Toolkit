from sanic import Sanic, Request, HTTPResponse, json
import devkit.sql as sql
import models

def attach_endpoints(app: Sanic):
    @app.get("/users")
    async def users(request: Request) -> HTTPResponse:
        users = sql.select_from(models.USER).fetch()

        return json([{
            "id": user.id,
            "name": user.name
        } for user in users])
    
    @app.get("/add_user")
    async def add_user(request: Request) -> HTTPResponse:
        models.User("Thomas", None, True)

        return json({})

def start():
    sql.set_sqlite_file("database.db")
    sql.set_debug(True)

    app = Sanic("App")

    attach_endpoints(app)
    
    return app

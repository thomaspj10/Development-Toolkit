from sanic import Sanic

import controllers.homepage

def start():
    app = Sanic("App")

    app.blueprint(controllers.homepage.bp)
    
    return app

import devkit.infra as infra

def generate_models():
    import devkit.sql as sql

    sql.generate_models()

def start():
    import app
    from sanic import Sanic
    from sanic.worker.loader import AppLoader

    loader = AppLoader(factory=app.start)
    app = loader.load()
    app.prepare(port=9999) # type: ignore
    Sanic.serve(primary=app, app_loader=loader)

with infra.define(__name__) as definition:
    definition.task("start", "Start the application.", [generate_models, start])

    definition.use_migrations()

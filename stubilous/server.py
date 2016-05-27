from flask import Flask, make_response
from stubilous.config import Config


def create_app():
    return Flask(__name__)


def default_view(body: str, status: int=200, headers: list=None, *args, **kwargs):
    response = make_response(body, status)
    if headers:
        response.headers = headers
    return response


def wrap(fn):
    import uuid
    fn.__name__ = str(uuid.uuid4())
    return fn


def init_routes(app: Flask, routes: list):
    from functools import partial
    for route in routes:
        app.add_url_rule(route.path,
                         methods=[route.method],
                         view_func=wrap(partial(default_view,
                                                route.body,
                                                route.status,
                                                route.headers)))


def run(args):
    import yaml
    with open(args.config, "r") as f:
        config = Config.from_dict(yaml.load(f))

    app = create_app()
    init_routes(app, config.routes)

    app.run(config.host, config.port)

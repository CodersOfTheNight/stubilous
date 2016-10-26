from flask import Flask, make_response


def create_app():
    return Flask(__name__)


def default_view(body, status=200, headers=None, cookies=None, **kwargs):
    response = make_response(body(**kwargs), status)
    if headers:
        response.headers = headers

    if cookies:
        response.cookies = cookies
    return response


def wrap(fn):
    import uuid
    fn.__name__ = str(uuid.uuid4())
    return fn


def init_routes(app, routes):
    from functools import partial
    for route in routes:
        app.add_url_rule(route.path,
                         methods=[route.method],
                         view_func=wrap(partial(default_view,
                                                route.body,
                                                route.status,
                                                route.headers)))


def run(config):
    app = create_app()
    init_routes(app, config.routes)
    app.run(host=config.host, port=config.port)

from functools import partial


def response(cls, method, url, body, status=200):
    from stubilous.config import Route
    route = Route(method=method, path=url, body=body, status=status)
    cls.routes.append(route)
    return cls


class Builder(object):

    def __init__(self):
        self.host = None
        self.port = None
        self.routes = []

    def server(self, host, port):
        self.host = host
        self.port = port
        return self

    def route(self, method, url):
        return partial(response, cls=self, method=method, path=url)

    def build(self):
        from stubilous.config import Config
        return Config(host=self.host,
                      port=self.port,
                      routes=self.routes)

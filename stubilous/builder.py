from functools import partial
from stubilous.config import Route


def response(callback,
             method,
             url,
             body,
             status=200,
             headers=None,
             cookies=None):

    callback(Route(method=method,
                   path=url,
                   body=body,
                   status=status,
                   desc="",
                   headers=headers,
                   cookies=cookies))


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
        def callback(route):
            self.routes.append(route)
            return self

        return partial(response, callback, method, url)

    def build(self):
        from stubilous.config import Config
        return Config(host=self.host,
                      port=self.port,
                      routes=self.routes)

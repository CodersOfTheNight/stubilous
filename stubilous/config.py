class Route(object):

    @staticmethod
    def from_dict(data: dict):
        return Route(desc=data.get("desc"),
                     method=data["method"],
                     path=data["path"],
                     status=data["status"],
                     body=data.get("body"),
                     file=data.get("file"),
                     headers=data.get("headers")
                     )

    def __init__(self,
                 desc: str,
                 method: str,
                 path: str,
                 status: int=200,
                 body: str=None,
                 file: str=None,
                 headers: list=None):
        self.desc = desc
        self.method = method
        self.path = path
        self.status = status
        if file:
            with open(self.file, "r") as f:
                self._body = f.read()
        else:
            self._body = body

        self.headers = headers

    def body(self, **kwargs):
        from jinja2 import Template
        tmpl = Template(self._body)
        return tmpl.render(kwargs)


class Config(object):

    @staticmethod
    def from_dict(data: dict):
        server = data["server"]
        return Config(host=server["host"],
                      port=server["port"],
                      routes=server["routes"])

    def __init__(self, host: str, port: int, routes: list):
        self.host = host
        self.port = port
        self.routes = [Route.from_dict(r)
                       for r in routes]

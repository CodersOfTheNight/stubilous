class Route(object):

    @staticmethod
    def from_dict(data):
        return Route(desc=data.get("desc"),
                     method=data["method"],
                     path=data["path"],
                     status=data["status"],
                     body=data.get("body"),
                     file=data.get("file"),
                     headers=data.get("headers"),
                     cookies=data.get("cookies")
                     )

    def __init__(self,
                 desc,
                 method,
                 path,
                 status=200,
                 body=None,
                 file=None,
                 headers=None,
                 cookies=None):
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
        self.cookies = cookies

    def body(self, **kwargs):
        from jinja2 import Template
        tmpl = Template(self._body)
        return tmpl.render(kwargs)


class Config(object):

    @staticmethod
    def from_dict(data):
        server = data["server"]
        routes = [Route.from_dict(r)
                  for r in server["routes"]]

        return Config(host=server["host"],
                      port=server["port"],
                      routes=routes)

    def __init__(self, host, port, routes):
        self.host = host
        self.port = port
        self.routes = routes

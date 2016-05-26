class Route(object):

    @staticmethod
    def from_dict(data: dict):
        return Route(desc=data.get("desc"),
                     method=data["method"],
                     path=data["path"],
                     body=data.get("body"),
                     file=data.get("file"),
                     headers=data.get("headers")
                     )

    def __init__(self,
                 desc: str,
                 method: str,
                 path: str,
                 body: str=None,
                 file: str=None,
                 headers: list=None):
        self.desc = desc
        self.method = method
        self.path = path
        if file:
            with open(self.file, "r") as f:
                self.body = f.read()
        else:
            self.body = body

        self.headers = headers


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

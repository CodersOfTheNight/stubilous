class Config(object):

    @staticmethod
    def from_dict(data: dict):
        server = data["server"]
        return Config(host=server["host"],
                      port=server["port"])

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

from pytest import fixture

from stubilous.config import Config


@fixture
def config_file() -> str:
    return """
---
server:
  port: 80
  host: localhost
  routes:
      - desc: A test route
        method: GET
        path: /test
        body: Hello!
        status: 200
"""


@fixture
def basic_config(config_file) -> Config:
    from io import StringIO
    import yaml
    buff = StringIO()
    buff.write(config_file)
    buff.seek(0)
    return Config.from_dict(yaml.load(buff))


def test_service_config(basic_config):
    assert basic_config.port == 80
    assert basic_config.host == "localhost"


def test_route_config(basic_config):
    routes = basic_config.routes
    assert routes[0].method == "GET"
    assert routes[0].path == "/test"
    assert routes[0].body == "Hello!"

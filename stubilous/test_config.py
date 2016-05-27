from pytest import fixture

from stubilous.config import Config


@fixture
def config_file():
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
      - desc: Advanced route
        method: GET
        path: /test/<name>
        body: Hello {{name}}!
        status: 200
"""


@fixture
def basic_config(config_file):
    from six import StringIO
    import yaml
    buff = StringIO()
    buff.write(config_file)
    buff.seek(0)
    return Config.from_dict(yaml.load(buff))


def test_service_config(basic_config):
    assert basic_config.port == 80
    assert basic_config.host == "localhost"


def test_route_config(basic_config):
    route = basic_config.routes[0]
    assert route.method == "GET"
    assert route.path == "/test"
    assert route.body() == "Hello!"


def test_template_route(basic_config):
    route = basic_config.routes[1]
    assert route.method == "GET"
    assert route.body(name="test") == "Hello test!"

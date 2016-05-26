from pytest import fixture

from stubilous.config import Config


@fixture
def config_file() -> str:
    return """
---
server:
  port: 80
  host: localhost
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

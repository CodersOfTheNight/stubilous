from pytest import fixture

from stubilous.config import Config


@fixture
def basic_config() -> Config:
    from io import StringIO
    import yaml
    buff = StringIO()
    buff.write("""
    ---
    server:
      port: 80
      host: localhost
    """)
    return Config.from_dict(yaml.load(buff))


def test_service_config(basic_config):
    server = basic_config()
    assert server.port == 80
    assert server.host == "localhost"

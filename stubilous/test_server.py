from pytest import fixture
from stubilous.builder import Builder


@fixture(scope="module")
def server(request):
    def on_close():
        pass

    request.addfinalizer(on_close)


def test_builder_server():
    builder = Builder()
    builder.server("localhost", 9999)
    config = builder.build()

    assert config.host == "localhost"
    assert config.port == 9999


def test_builder_routes():
    builder = Builder()
    builder.route("GET", "/hello")("Hello world!")
    config = builder.build()
    route = config.routes[0]

    assert route.status == 200
    assert route.body() == "Hello world!"
    assert route.method == "GET"

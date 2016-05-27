import logging
from pytest import fixture
from stubilous.builder import Builder
logging.basicConfig(level=logging.DEBUG)


@fixture(scope="session")
def server(request):
    from multiprocessing import Process
    from stubilous.server import run
    builder = Builder()
    builder.server(host="localhost", port=9999)
    builder.route("GET", "/hello/<name>")("Hello {{ name }}!", 200)

    config = builder.build()
    proc = Process(target=run, args=(config,))

    def on_close():
        proc.terminate()
        proc.join()

    request.addfinalizer(on_close)
    proc.start()
    return proc


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


def test_server_greeting(server):
    import requests
    result = requests.get("http://localhost:9999/hello/world")

    assert result.text == "Hello world!"

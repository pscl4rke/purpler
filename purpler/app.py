

import os

from quart import Quart, make_response

import aguirre.integrations.quart as aguirre_quart
from events import event_producer


APP = Quart("purpler")
APP.register_blueprint(aguirre_quart.create_blueprint("vendor"),
                       url_prefix="/vendor")


def load_from_file(basedir: str, path: str) -> str:
    with open(os.path.join(basedir, path)) as f:
        return f.read()


@APP.route("/")
async def home():
    #return "Hello World"
    return load_from_file(".", "home.html")


@APP.route("/events")
async def events():
    response = await make_response(event_producer(), {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        "Transfer-Encoding": "chunked",
    })
    response.timeout = None
    return response


@APP.route("/asset/<path:path>")
async def asset(path: str):
    return load_from_file("asset", path)


if __name__ == "__main__":
    APP.run()

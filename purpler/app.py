

import os
import tarfile

from quart import Quart, make_response
from aguirre.util import guess_mime_type, load_from_tarball

from events import event_producer


APP = Quart("purpler")


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


@APP.route("/vendor/<string:pkgname>/<path:path>")
async def vendor(pkgname: str, path: str):
    content = load_from_tarball("vendor/" + pkgname + ".tar.gz", "package/" + path)
    response = await make_response(content)
    response.mimetype = guess_mime_type(path)
    return response


if __name__ == "__main__":
    APP.run()

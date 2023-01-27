

import os

from quart import Quart


APP = Quart("purpler")


def load_from_file(basedir: str, path: str) -> str:
    with open(os.path.join(basedir, path)) as f:
        return f.read()


@APP.route("/")
async def home():
    #return "Hello World"
    return load_from_file(".", "home.html")


@APP.route("/asset/<path:path>")
async def asset(path):
    return load_from_file("asset", path)


if __name__ == "__main__":
    APP.run()

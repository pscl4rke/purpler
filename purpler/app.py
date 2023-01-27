

import os
import tarfile

from quart import Quart


APP = Quart("purpler")


def load_from_file(basedir: str, path: str) -> str:
    with open(os.path.join(basedir, path)) as f:
        return f.read()


def load_from_tarball(tarball: str, path: str) -> str:
    with tarfile.open(tarball, "r:gz") as archive:
        #member = archive.getmember(path)
        src = archive.extractfile(path)
        return src.read()


@APP.route("/")
async def home():
    #return "Hello World"
    return load_from_file(".", "home.html")


@APP.route("/asset/<path:path>")
async def asset(path: str):
    return load_from_file("asset", path)


@APP.route("/vendor/<string:pkgname>/<path:path>")
async def vendor(pkgname: str, path: str):
    return load_from_tarball("vendor/" + pkgname + ".tar.gz", "package/" + path)


if __name__ == "__main__":
    APP.run()

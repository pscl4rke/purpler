

from quart import Blueprint, make_response
from aguirre.util import guess_mime_type, load_from_tarball


BLUEPRINT = Blueprint("aguirre", "aguirre")


@BLUEPRINT.route("/<package>@<version>/<path:resourcepath>")
async def vendor(package: str, version: str, resourcepath: str):
    srcpath = f"vendor/{package}@{version}.tar.gz"
    content = load_from_tarball(srcpath, f"package/{resourcepath}")
    response = await make_response(content)
    response.mimetype = guess_mime_type(resourcepath)
    return response

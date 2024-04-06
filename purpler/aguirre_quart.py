

import quart
from quart.typing import ResponseReturnValue as Rsp
from aguirre.util import guess_mime_type, load_from_tarball


async def view(basedir: str, package: str, version: str, resourcepath: str) -> Rsp:
    srcpath = f"{basedir}/{package}@{version}.tar.gz"
    content = load_from_tarball(srcpath, f"package/{resourcepath}")
    if content is None:
        return quart.abort(404)
    response = await quart.make_response(content)
    response.mimetype = guess_mime_type(resourcepath)
    return response


def create_blueprint(basedir: str) -> quart.Blueprint:
    blueprint = quart.Blueprint("aguirre", "aguirre")
    blueprint.add_url_rule(
        "/<package>@<version>/<path:resourcepath>",
        view_func=view,
        defaults={"basedir": basedir},
    )
    return blueprint

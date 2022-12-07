from flask import Blueprint, request

from backend.services import vowel
from backend.api.decorators import datarequired

blueprint_api = Blueprint("api", __name__, url_prefix="/api")


@blueprint_api.route("/vowel_count", methods=["POST"])
@datarequired({"words": (list, True)})
def vowel_count():
    resp = vowel.count(request.params_schema["words"])
    return resp, 200

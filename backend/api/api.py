from flask import Blueprint, request

from backend.services import vowel, sort
from backend.api.decorators import datarequired

blueprint_api = Blueprint("api", __name__, url_prefix="/api")


@blueprint_api.route("/vowel_count", methods=["POST"])
@datarequired({"words": (list, True)})
def vowel_count():
    resp = vowel.count(request.params_schema["words"])
    return resp, 200


@blueprint_api.route("/sort", methods=["POST"])
@datarequired({"words": (list, True), "order": (str, True)})
def sorter():
    words = request.params_schema["words"]
    order = request.params_schema["order"]
    resp = sort.sort(words, order)
    return resp, 200

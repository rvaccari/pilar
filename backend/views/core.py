from flask import Blueprint

blueprint_core = Blueprint("core", __name__)


@blueprint_core.route("/", methods=["GET"])
def home():
    return "Home"

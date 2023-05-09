import datetime
from flask import jsonify, Blueprint, request
from .uf_service import get_uf_value
from api.error_handling.errors import BadRequestError
from api.util.parse_date import parse_date


uf_blueprint = Blueprint("uf", __name__)

@uf_blueprint.route("/uf", methods=["GET"])
def get_uf():
    date_str = request.args.get("date")
    date = parse_date(date_str)
    if date < datetime.datetime(2013, 1, 1):
        raise BadRequestError("Fecha mínima permitida: 01-01-2013")
    uf_value = get_uf_value(date)
    return jsonify({"date": date_str, "value": uf_value})

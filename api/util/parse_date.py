import datetime
from api.error_handling.errors import BadRequestError


def parse_date(date_str):
    if not date_str:
        raise BadRequestError("Fecha no proporcionada")
    try:
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return date
    except ValueError:
        raise BadRequestError("Formato de fecha inválido")

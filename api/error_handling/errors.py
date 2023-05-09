from flask import jsonify


class APIError(Exception):
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def to_response(self):
        response = jsonify({"error": self.message})
        response.status_code = self.status_code
        return response


class BadRequestError(APIError):
    status_code = 400


class NotFoundError(APIError):
    status_code = 404

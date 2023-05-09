from flask import Flask
from api.error_handling.error_handler import handle_error
from api.error_handling.errors import APIError
from api.uf.uf_controller import uf_blueprint


app = Flask(__name__)
app.register_error_handler(APIError, handle_error)
app.register_blueprint(uf_blueprint)

if __name__ == "__main__":
    app.run()

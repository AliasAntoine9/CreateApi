"""Create an API with Flask: Flask wrapper"""
from flask import Flask

from endpoints.vetchain import create_closed_position


api = Flask(__name__)

api.add_url_rule("/api/v1/create_closed_position", endpoint="create_closed_position", view_func=create_closed_position, methods=["POST"])

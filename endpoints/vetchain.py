from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

import table_handler.vetchain as vetchain
from table_handler.vetchain import add_closed_position

api = Flask(__name__)


@api.route("/api/v1/create_closed_position", methods=["POST"])
def create_closed_position():
	"""This method insert a new closed position in the BDD"""
	payload = request.get_json()
	try:
		result = add_closed_position(**payload)
	except TypeError as error:
		sentence = "() got an unexpected keyword argument"
		if isinstance(error, TypeError) and sentence in str(error):
			splited_error = str(error).split(sentence)
			wrong_argument = splited_error[1]
			function_name = splited_error[0]
			valid_arguments = sorted(getattr(vetchain, function_name).__code__.co_consts[1])
			return f"Invalid argument: {wrong_argument} provided.\nValid arguments are: {valid_arguments}", 500

	if result:
		return jsonify(status="True", message="New closed position inserted !")
	return jsonify(status="False", message="Error while inserting")


# This function manage 500 Error (Internal Server Error)
@api.errorhandler(Exception)
def handle_bad_request(error):
	if isinstance(error, HTTPException):
		return error
	return str(error), 500

import os
from dotenv import load_dotenv
from slack import WebClient
from flask import request,jsonify
from flask_api import FlaskAPI
from .actions import  WebActions
load_dotenv()


if not os.environ.get("SLACK_BOT_TOKEN"):
    raise Exception("[!] SLACK_BOT_TOKEN environment variable is not set")

slack_client = WebClient(os.environ.get("SLACK_BOT_TOKEN"))
app = FlaskAPI(__name__, instance_relative_config=False)


@app.route("/server-monitor", methods=["POST"])
def server_monitor():
    command_text = request.data.get('text')
    command_text = command_text.split(' ')
    slack_uid = request.data.get('user_id')
    if command_text[0] == "help":
        response = "This is the help message"
    response = {'text': "Hello from Server Monitor Bot"}
    response = jsonify(response)
    response.status_code = 200
    return response

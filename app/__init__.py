import os
from dotenv import load_dotenv
from slack import WebClient
from flask import request, jsonify
from flask_api import FlaskAPI
from .actions import WebActions

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
    response = "Hello from Server Monitor Bot"
    if command_text[0] == "help":
        response = "This is the help message"
    response = {'text': response}
    response = jsonify(response)
    response.status_code = 200
    return response


@app.route("/check-server", methods=["POST"])
def check_server():
    command = request.data.get('text').split(" ")
    if not 'http://' in command[-1] or not 'https://' in command[-1]:
        response = jsonify({
            'text': f'The url {command[-1]} is not correct ',
        })
        response.status_code = 200
        return response
    response = jsonify({
        'text': WebActions(url=command[-1]).check_website_status()
    })
    response.status_code = 200
    return response
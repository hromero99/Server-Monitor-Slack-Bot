import os
from dotenv import load_dotenv
from slack import WebClient
from flask import request, jsonify
from flask_api import FlaskAPI
from .actions import WebActions
from .database import Database

load_dotenv()

if not os.environ.get("SLACK_BOT_TOKEN"):
    raise Exception("[!] SLACK_BOT_TOKEN environment variable is not set")
if not os.environ.get("DATABASE_FILE"):
    raise Exception("[!] Json File for database path is not set")

slack_client = WebClient(os.environ.get("SLACK_BOT_TOKEN"))
app = FlaskAPI(__name__, instance_relative_config=False)
database = Database(os.environ.get("DATABASE_FILE"))

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

    if command[0] == 'add':
        database.add_new_server(server_url=command[-1])
        response = jsonify({
            'text': f'Url {command[-1]} agregada correctamente'
        })
    elif command[0] == 'check':
        checker = WebActions()
        status = []
        for server in database.get_urls():
            status.append(
                f'{server} -->  {checker.check_website_status(url=server)}'
            )
        response = jsonify({
            'text': '\n'.join(status)
        })
    else:
        response = jsonify({
            'text': f'Error al ejecutar el comando {command[0]}'
        })
    response.status_code = 200
    return response

import os
from dotenv import load_dotenv
from slack import WebClient
load_dotenv()

if not os.environ.get("SLACK_BOT_TOKEN"):
    raise Exception("[!] SLACK_BOT_TOKEN environment variable is not set")

slack_client = WebClient(os.environ.get("SLACK_BOT_TOKEN"))
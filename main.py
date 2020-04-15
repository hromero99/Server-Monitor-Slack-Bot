from app import slack_client
from app import WebActions
import time
import sys
import json
from multiprocessing import Process
from app import app

def testing_web(url: str):
    print(f"[?] Testing {url}")
    status = WebActions(url).check_website_status()
    if status is not True:
        slack_client.chat_postMessage(
            channel="#servernotifications",
            text=status
        )


def distribute_jobs(json_path: str):

    processes = []
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    for url in data.get("sites"):
        process = Process(target=testing_web, args=(url,))
        processes.append(process)
        process.start()

    [proc.join() for proc in processes]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py configFile.json")
        exit(-1)
    app.run(host='0.0.0.0')
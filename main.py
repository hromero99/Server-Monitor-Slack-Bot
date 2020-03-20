from app import slack_client
from app import WebActions
import schedule
import time
import sys


def testing_web(url: str):
    print(f"[?] Testing {url}")
    status = WebActions(url).check_website_status()
    if status is not True:
        slack_client.chat_postMessage(
            channel="#servernotifications",
            text=status
        )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py url")
        exit(-1)

    schedule.every(5).minutes.do(testing_web, (sys.argv[1]))
    while 1:
        schedule.run_pending()
        time.sleep(1)

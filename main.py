from app import slack_client
from app import WebActions

if __name__ == "__main__":
    if WebActions("http://54.159.185.30:8000/").check_website_status() is not True:
        slack_client.chat_postMessage(
            channel="#servernotifications",
            text="[!] Notificacion de prueba"
        )

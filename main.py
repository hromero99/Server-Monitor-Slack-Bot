from app import slack_client

if __name__ == "__main__":
    slack_client.chat_postMessage(
        channel="#ServerNotifications",
        text="[!] Notificacion de prueba"
    )
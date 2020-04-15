import requests


class WebActions(object):

    @staticmethod
    def check_website_status(url: str) -> [str]:
        try:
            r = requests.get(url=url,)
            return f'[:)] SUCESS {r.status_code}'
        except requests.exceptions.ConnectionError as error:
            return f"[!] Error while connecting to server {error}"

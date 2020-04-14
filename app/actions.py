import requests


class WebActions(object):
    def __init__(self, url: str):
        self.url = url

    def check_website_status(self) -> [bool, str]:
        try:
            r = requests.get(url=self.url)
            return r.status_code
        except requests.exceptions.ConnectionError as error:
            return f"[!] Error While connecting to server {error}"

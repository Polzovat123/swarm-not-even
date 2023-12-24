import requests


class DatsteamAPI:
    def __init__(self, base_url="https://datsblack.datsteam.dev/api", api_key=""):
        self.base_url = base_url
        self.headers = {"X-API-Key": api_key}

    def scan(self):
        url = f"{self.base_url}/scan"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_map(self):
        url = f"{self.base_url}/map"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def send_ship_commands(self, ship_commands):
        url = f"{self.base_url}/shipCommand"
        payload = ship_commands
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()


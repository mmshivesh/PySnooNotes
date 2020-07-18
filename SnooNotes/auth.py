import time
import urllib

import requests


class SnooNotesAuth:
    def __init__(self, username, user_key):
        self.username = username
        self.user_key = user_key
        self.base_url = "https://snoonotes.com/"

    def get_access_token(self):

        url = urllib.parse.urljoin(self.base_url, "/auth/connect/token")
        r = requests.post(url, data={
            "grant_type": "password",
            "username": self.username,
            "password": self.user_key,
            "client_id": "bots"
        })
        if r.ok:
            print(f"Authenticated as user: {self.username}")
            response = r.json()
            self.access_token = response['access_token']
            self.expire_time = round(time.time()) + response['expires_in']
            self.token_type = response['token_type']
        else:
            print(f"Failed with code: {r.status_code}")

    def refresh_access_token(self):
        if round(time.time()) > self.expire_time:
            print("Token expired, refreshing.")
            self.get_access_token()
        else:
            return

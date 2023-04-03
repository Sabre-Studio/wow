import os
from datetime import datetime

import pytz
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from mplus_svc.external.blizz_api.model import BlizzAuthToken

load_dotenv()

BLIZZ_CLIENT = os.getenv("BLIZZ_CLIENT_ID")
BLIZZ_SECRET = os.getenv("BLIZZ_CLIENT_SECRET")
BLIZZ_AUTH_URL = "https://oauth.battle.net/token"


class BlizzardApiAuth:
    def __init__(self):
        self.token = BlizzardApiAuth.fetch_auth_token()

    def get_token(self) -> BlizzAuthToken:
        print(self.token)
        if self.is_token_expired():
            print("token expired, making a new one")
            self.token = BlizzardApiAuth.fetch_auth_token()

        return self.token

    def is_token_expired(self) -> bool:
        return datetime.now(tz=pytz.utc) > self.token.expires_at

    @staticmethod
    def fetch_auth_token() -> BlizzAuthToken:
        client = BackendApplicationClient(client_id=BLIZZ_CLIENT)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url=BLIZZ_AUTH_URL, client_id=BLIZZ_CLIENT, client_secret=BLIZZ_SECRET
        )

        blizz_token = BlizzAuthToken.parse_obj(token)
        print(f"made new token: {blizz_token}")
        return blizz_token

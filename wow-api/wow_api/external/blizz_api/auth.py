from pydantic import BaseModel, ValidationError
import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from datetime import datetime, timedelta
from dotenv import load_dotenv
import pytz

load_dotenv()


class BlizzAuthToken(BaseModel):
    access_token: str
    token_type: str
    expires_in: timedelta
    sub: str
    expires_at: datetime


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
        BLIZZ_CLIENT = os.getenv("BLIZZ_CLIENT_ID")
        BLIZZ_SECRET = os.getenv("BLIZZ_CLIENT_SECRET")
        auth_url = "https://oauth.battle.net/token"
        client = BackendApplicationClient(client_id=BLIZZ_CLIENT)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url=auth_url, client_id=BLIZZ_CLIENT, client_secret=BLIZZ_SECRET
        )

        try:
            blizz_token: BlizzAuthToken = BlizzAuthToken.parse_obj(token)
            print(f"made new token: {blizz_token}")
        except ValidationError as e:
            print(e)

        return blizz_token

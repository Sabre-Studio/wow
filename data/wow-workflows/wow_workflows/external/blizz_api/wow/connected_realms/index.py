from pydantic import BaseModel
import requests

from wow_api.external.blizz_api.auth import BlizzAuthToken

class Self(BaseModel):
    href: str


class _Links(BaseModel):
    self: Self


class ConnectedRealm(BaseModel):
    href: str


class ConnectedRealmsIndexResponse(BaseModel):
    _links: _Links
    connected_realms: list[ConnectedRealm]

def get_connected_realms_index(token: BlizzAuthToken) -> ConnectedRealmsIndexResponse:
    url = 'https://us.api.blizzard.com/data/wow/connected-realm/index?namespace=dynamic-us&locale=en_US'

    res = requests.get(url, headers= {
        'Authorization': f'Bearer: {token.access_token}'
    })

    return ConnectedRealmsIndexResponse.parse_obj(res)


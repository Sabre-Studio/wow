from wow_api.external.blizz_api.auth import BlizzardApiAuth
from wow_api.external.blizz_api.wow.connected_realms.index import (
    get_connected_realms_index,
)

api_auth = BlizzardApiAuth()

connected_realm_index = get_connected_realms_index(api_auth.get_token())


with open("./data/realms.json", "w") as f:
    f.write(connected_realm_index.json(indent=2))

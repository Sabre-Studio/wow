from wow_api.external.blizz_api.auth import BlizzardApiAuth
from wow_api.external.blizz_api.game.connected_realm import get_connected_realm_by_id

api_auth = BlizzardApiAuth()


proudmoore_realm = get_connected_realm_by_id(5, api_auth.get_token())

with open("./data/proudmoore.json", "w") as f:
    f.write(proudmoore_realm.json(indent=2))

from enum import StrEnum, auto
from time import sleep

import requests
from dotenv import load_dotenv
from pydantic import BaseModel, Field, HttpUrl

from wow_api.external.blizz_api.auth import BlizzardApiAuth

load_dotenv()


class BlizzardApiRegion(StrEnum):
    us = auto()
    eu = auto()
    kr = auto()
    tw = auto()


class BlizzardNamespaceCategory(StrEnum):
    static = auto()
    dynamic = auto()
    profile = auto()


class BlizzardApiLocales(StrEnum):
    en_us = "en_US"
    es_mx = "es_MX"
    pt_br = "pt_BR"
    de_de = "de_DE"
    en_gb = "en_GB"
    es_es = "es_ES"
    fr_fr = "fr_FR"
    it_it = "it_IT"
    ru_RU = "ru_RU"
    ko_kr = "ko_KR"
    zh_tw = "zh_TW"
    zh_cn = "zh_CN"


class Self(BaseModel):
    href: HttpUrl


class FieldLinks(BaseModel):
    self: Self


class ConnectedRealm(BaseModel):
    href: HttpUrl


class ConnectedRealmsListResponse(BaseModel):
    field_links: FieldLinks = Field(..., alias="_links")
    connected_realms: list[ConnectedRealm]


class Status(BaseModel):
    type: str
    name: str


class Population(BaseModel):
    type: str
    name: str


class Key(BaseModel):
    href: HttpUrl


class Region(BaseModel):
    key: Key
    name: str
    id: int


class Type(BaseModel):
    type: str
    name: str


class Realm(BaseModel):
    id: int
    region: Region
    connected_realm: ConnectedRealm
    name: str
    category: str
    locale: str
    timezone: str
    type: Type
    is_tournament: bool
    slug: str


class MythicLeaderboards(BaseModel):
    href: HttpUrl


class Auctions(BaseModel):
    href: HttpUrl


class ConnectedRealmResponse(BaseModel):
    field_links: FieldLinks = Field(..., alias="_links")
    id: int
    has_queue: bool
    status: Status
    population: Population
    realms: list[Realm]
    mythic_leaderboards: MythicLeaderboards
    auctions: Auctions


class CurrentLeaderboard(BaseModel):
    key: Key
    name: str
    id: int


class RealmCurrentLeaderboardsResponse(BaseModel):
    field_links: FieldLinks = Field(..., alias="_links")
    current_leaderboards: list[CurrentLeaderboard]


class Map(BaseModel):
    name: str
    id: int


class ProfileRealm(BaseModel):
    key: Key
    id: int
    slug: str


class Profile(BaseModel):
    name: str
    id: int
    realm: ProfileRealm


class Faction(BaseModel):
    type: str


class Specialization(BaseModel):
    key: Key
    id: int


class Member(BaseModel):
    profile: Profile
    faction: Faction
    specialization: Specialization


class Color(BaseModel):
    r: int
    g: int
    b: int
    a: float


class MythicRating(BaseModel):
    color: Color
    rating: float


class LeadingGroup(BaseModel):
    ranking: int
    duration: int
    completed_timestamp: int
    keystone_level: int
    members: list[Member]
    mythic_rating: MythicRating


class KeystoneAffix(BaseModel):
    key: Key
    name: str
    id: int


class CurrentAffix(BaseModel):
    keystone_affix: KeystoneAffix
    starting_level: int


class LeaderboardResponse(BaseModel):
    field_links: FieldLinks = Field(..., alias="_links")
    map: Map
    period: int
    period_start_timestamp: int
    period_end_timestamp: int
    connected_realm: ConnectedRealm
    leading_groups: list[LeadingGroup] | None
    keystone_affixes: list[CurrentAffix]
    map_challenge_mode_id: int
    name: str


api_auth = BlizzardApiAuth()
token = api_auth.get_token()

default_region: BlizzardApiRegion = BlizzardApiRegion.us
default_locale: BlizzardApiLocales = BlizzardApiLocales.en_us

default_params = {"locale": default_locale.value}


def build_url(endpoint: str, region: BlizzardApiRegion = default_region) -> str:
    return f"https://{region.value}.api.blizzard.com{endpoint}"


def build_headers(
    namespace_category: BlizzardNamespaceCategory | None = None,
    region: BlizzardApiRegion = default_region,
) -> dict[str, str]:
    if namespace_category:
        return {
            "Authorization": f"Bearer {token.access_token}",
            "Battlenet-Namespace": f"{namespace_category.value}-{region.value}",
        }

    else:
        return {
            "Authorization": f"Bearer {token.access_token}",
        }


def get_url_params(url: HttpUrl) -> dict[str, str]:
    query_string = url.query
    query_params = query_string.split("&")
    print(query_params)

    param_dict = {}
    for p in query_params:
        key_value = p.split("=")
        if len(key_value) > 0:
            param_dict[key_value[0]] = key_value[1]

    return param_dict


def get_connected_realms_list(
    locale: BlizzardApiLocales = default_locale,
) -> ConnectedRealmsListResponse:
    url = build_url("/data/wow/connected-realm/index")

    connected_realms_res = requests.get(
        url,
        headers=build_headers(BlizzardNamespaceCategory.dynamic),
        params={"locale": locale.value},
    )

    return ConnectedRealmsListResponse.parse_obj(connected_realms_res.json())


def throttle(msg: str):
    print(msg)
    sleep(1)


oce_realms = [
    {
        "id": 3725,
        "mythic_leaderboards_href": "https://us.api.blizzard.com/data/wow/connected-realm/3725/mythic-leaderboard/?namespace=dynamic-us",
    },
    {
        "id": 3726,
        "mythic_leaderboards_href": "https://us.api.blizzard.com/data/wow/connected-realm/3726/mythic-leaderboard/?namespace=dynamic-us",
    },
]
for cr in oce_realms:
    mythic_leaderboards_res = requests.get(
        cr["mythic_leaderboards_href"],
        headers=build_headers(),
        params=default_params,
    )
    print(mythic_leaderboards_res.headers)

    throttle(f"get leaderboard for {cr['id']}")

    leaderboards = RealmCurrentLeaderboardsResponse.parse_obj(
        mythic_leaderboards_res.json()
    )

    with open(f"./out/current-leaderboards/{cr['id']}.json", "w") as file:
        file.write(leaderboards.json(indent=2))

    for l in leaderboards.current_leaderboards:
        leaderboard_req = requests.get(
            l.key.href, headers=build_headers(), params=default_params
        )
        print(leaderboard_req.headers)

        leaderboard = LeaderboardResponse.parse_obj(leaderboard_req.json())
        throttle(f"get {leaderboard.name} for {cr['id']}")

        dungeon_name = leaderboard.name.lower().replace(" ", "-")
        file_name = f"./out/leaderboards/{cr['id']}-{dungeon_name}-period-{leaderboard.period}.json"

        with open(
            file_name,
            "w",
        ) as file:
            file.write(leaderboard.json(indent=2))

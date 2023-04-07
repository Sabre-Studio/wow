from enum import StrEnum, auto

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


api_auth = BlizzardApiAuth()
token = api_auth.get_token()

default_region: BlizzardApiRegion = BlizzardApiRegion.us
default_locale: BlizzardApiLocales = BlizzardApiLocales.en_us


def build_url(endpoint: str, region: BlizzardApiRegion = default_region) -> str:
    return f"https://{region.value}.api.blizzard.com{endpoint}"


def build_headers(
    namespace_category: BlizzardNamespaceCategory,
    region: BlizzardApiRegion = default_region,
) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token.access_token}",
        "Battlenet-Namespace": f"{namespace_category.value}-{region.value}",
    }


class Self(BaseModel):
    href: HttpUrl


class FieldLinks(BaseModel):
    self: Self


class ConnectedRealm(BaseModel):
    href: HttpUrl


class ConnectedRealmsListResponse(BaseModel):
    field_links: FieldLinks = Field(..., alias="_links")
    connected_realms: list[ConnectedRealm]


def get_connected_realms_list() -> ConnectedRealmsListResponse:
    url = build_url("/data/wow/connected-realm/index")


def get_connected_realm():
    url = "/data/wow/connected-realm/{connected_realm_id}"


def get_mythic_keystone_leaderboard_list():
    url = "/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/index"


def get_mythic_keystone_leaderboard():
    url = "/data/wow/connected-realm/{connected_realm_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}"


def get_spec_list():
    full_url = "https://us.api.blizzard.com/data/wow/playable-specialization/index?namespace=static-us&locale=en_US"
    url = "/data/wow/playable-specialization/index"


def get_spec():
    full_url = "https://us.api.blizzard.com/data/wow/playable-specialization/270?namespace=static-us&locale=en_US"
    url = "/data/wow/playable-specialization/{specId}"


def get_spec_media():
    url = "/data/wow/media/playable-specialization/{specId}"


def get_class_list():
    url = "/data/wow/playable-class/index"


def get_class():
    url = "/data/wow/playable-class/{classId}"


def get_class_media():
    url = "/data/wow/media/playable-class/{playableClassId}"


def get_races_list():
    url = "/data/wow/playable-race/index"


def get_race():
    url = "/data/wow/playable-race/{playableRaceId}"


def get_character_mythic_keystone_profile():
    url = "/profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile"


def get_character_mythic_keystone_season_details():
    url = "/profile/wow/character/{realmSlug}/{characterName}/mythic-keystone-profile/season/{seasonId}"


def get_character_profile():
    url = "/profile/wow/character/{realmSlug}/{characterName}"


def get_character_statistics():
    url = "/profile/wow/character/{realmSlug}/{characterName}/statistics"


def get_character_equipment():
    url = "/profile/wow/character/{realmSlug}/{characterName}/equipment"


def get_character_media():
    url = "/profile/wow/character/{realmSlug}/{characterName}/character-media"

import requests
from wow_api import WowApiModel
from wow_api.external.blizz_api.auth import BlizzAuthToken


class ConnectedRealmRegion(WowApiModel):
    id: int
    name: str


class RealmType(WowApiModel):
    name: str
    type: str


class ConnectedRealmStatus(WowApiModel):
    name: str
    type: str


class ConnectedRealmPopulation(WowApiModel):
    name: str
    type: str


class ConnectedRealmRealm(WowApiModel):
    id: int
    slug: str
    name: str
    timezone: str
    locale: str
    is_tournament: bool
    category: str
    type: RealmType
    region: ConnectedRealmRegion


class ConnectedRealmSearchResult(WowApiModel):
    id: int
    href: str
    status: ConnectedRealmStatus
    population: ConnectedRealmStatus
    has_queue: bool
    realms: list[ConnectedRealmRealm]


class ConnectedRealmSearchResponse(WowApiModel):
    page: int
    page_size: int
    max_page_size: int
    page_count: int
    results: list[ConnectedRealmSearchResult]


class ConnectedRealm(WowApiModel):
    id: int
    href: str
    has_queue: bool
    mythic_keystone_leaderboard_href: str
    auctions_href: str
    status: ConnectedRealmStatus
    population: ConnectedRealmPopulation
    realms: list[ConnectedRealmRealm]


class ConnectedRealmResponse(WowApiModel):
    connected_realm: ConnectedRealm


def get_connected_realm_search(token: BlizzAuthToken) -> ConnectedRealmSearchResponse:
    url = f"https://us.api.blizzard.com/data/wow/search/connected-realm?namespace=dynamic-us&status.type=UP&orderby=id&_page=1&access_token={token.access_token}"

    connected_realms_res = requests.get(url)

    realms_dict = connected_realms_res.json()

    connected_realms = []
    for rc in realms_dict["results"]:
        realms = []
        for r in rc["data"]["realms"]:
            realm: ConnectedRealmRealm = ConnectedRealmRealm(
                id=r["id"],
                slug=r["slug"],
                name=r["name"]["en_US"],
                timezone=r["timezone"],
                locale=r["locale"],
                is_tournament=r["is_tournament"],
                category=r["category"]["en_US"],
                type=RealmType(name=r["type"]["name"]["en_US"], type=r["type"]["type"]),
                region=ConnectedRealmRegion(
                    id=r["region"]["id"], name=r["region"]["name"]["en_US"]
                ),
            )
            realms.append(realm)

        connected_realm: ConnectedRealmSearchResult = ConnectedRealmSearchResult(
            id=rc["data"]["id"],
            href=rc["key"]["href"],
            has_queue=rc["data"]["has_queue"],
            status=ConnectedRealmStatus(
                name=rc["data"]["status"]["name"]["en_US"],
                type=rc["data"]["status"]["type"],
            ),
            population=ConnectedRealmPopulation(
                name=rc["data"]["population"]["name"]["en_US"],
                type=rc["data"]["population"]["type"],
            ),
            realms=realms,
        )
        connected_realms.append(connected_realm)

    search_response: ConnectedRealmSearchResponse = ConnectedRealmSearchResponse(
        page=realms_dict["page"],
        page_size=realms_dict["pageSize"],
        max_page_size=realms_dict["maxPageSize"],
        page_count=realms_dict["pageCount"],
        results=connected_realms,
    )

    return search_response


def get_connected_realm_by_id(
    connected_realm_id: int, token: BlizzAuthToken
) -> ConnectedRealmResponse:
    url = f"https://us.api.blizzard.com/data/wow/connected-realm/{connected_realm_id}?namespace=dynamic-us&locale=en_US&access_token={token.access_token}"

    connected_realm_res = requests.get(url)

    connected_realm_dict = connected_realm_res.json()

    print(connected_realm_dict)

    realms = []
    for r in connected_realm_dict["realms"]:
        realm: ConnectedRealmRealm = ConnectedRealmRealm(
            id=r["id"],
            slug=r["slug"],
            name=r["name"],
            timezone=r["timezone"],
            locale=r["locale"],
            is_tournament=r["is_tournament"],
            category=r["category"],
            type=RealmType(name=r["type"]["name"], type=r["type"]["type"]),
            region=ConnectedRealmRegion(id=r["region"]["id"], name=r["region"]["name"]),
        )
        realms.append(realm)

    connected_realm: ConnectedRealm = ConnectedRealm(
        id=connected_realm_dict["id"],
        href=connected_realm_dict["_links"]["self"]["href"],
        has_queue=connected_realm_dict["has_queue"],
        mythic_keystone_leaderboard_href=connected_realm_dict["mythic_leaderboards"][
            "href"
        ],
        auctions_href=connected_realm_dict["auctions"]["href"],
        status=ConnectedRealmStatus(
            name=connected_realm_dict["status"]["name"],
            type=connected_realm_dict["status"]["type"],
        ),
        population=ConnectedRealmPopulation(
            name=connected_realm_dict["population"]["name"],
            type=connected_realm_dict["population"]["type"],
        ),
        realms=realms,
    )

    return ConnectedRealmResponse(connected_realm=connected_realm)

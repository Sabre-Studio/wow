from pydantic import BaseModel, HttpUrl
from enum import StrEnum, auto


class RealmStatus(StrEnum):
    up = auto()
    down = auto()
    unknown = auto()


class RealmPopulation(StrEnum):
    full = auto()
    high = auto()
    medium = auto()
    low = auto()


class RealmType(StrEnum):
    normal = auto()
    pvp = auto()


class Region(BaseModel):
    id: int
    name: str
    href: HttpUrl


class Realm(BaseModel):
    id: int
    slug: str
    name: str
    type: RealmType
    category: str
    locale: str
    timezone: str
    is_tournament: bool
    region: Region
    connected_realm: "ConnectedRealm"


class ConnectedRealm(BaseModel):
    id: int
    status: RealmStatus
    population: RealmPopulation
    realms: Realm
    href: HttpUrl

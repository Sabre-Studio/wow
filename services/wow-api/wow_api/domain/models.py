from pydantic import BaseModel
from enum import StrEnum, auto


class BlizzardRegion(StrEnum):
    us = auto()
    eu = auto()
    kr = auto()
    tw = auto()


class AuthToken(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    sub: str
    expires_at: float


class Region(BaseModel):
    id: int
    name: str


class RealmType(BaseModel):
    name: str
    type: str


class RealmStatus(BaseModel):
    name: str
    type: str


class RealmPopulation(BaseModel):
    name: str
    type: str


class Realm(BaseModel):
    is_tournament: bool
    timezone: str
    name: str
    id: int
    region: Region
    category: str
    locale: str
    type: RealmType
    slug: str


class ConnectedRealm(BaseModel):
    href: str
    realms: list[Realm]
    id: int
    has_queue: bool
    status: RealmStatus
    population: RealmPopulation

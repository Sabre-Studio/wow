# generated by datamodel-codegen:
#   filename:  raw.json
#   timestamp: 2023-04-04T18:55:54+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Self(BaseModel):
    href: str


class FieldLinks(BaseModel):
    self: Self


class Status(BaseModel):
    type: str
    name: str


class Population(BaseModel):
    type: str
    name: str


class Key(BaseModel):
    href: str


class Region(BaseModel):
    key: Key
    name: str
    id: int


class ConnectedRealm(BaseModel):
    href: str


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
    href: str


class Auctions(BaseModel):
    href: str


class Model(BaseModel):
    field_links: FieldLinks = Field(..., alias='_links')
    id: int
    has_queue: bool
    status: Status
    population: Population
    realms: List[Realm]
    mythic_leaderboards: MythicLeaderboards
    auctions: Auctions

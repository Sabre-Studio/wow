import sqlalchemy as sql
import sqlalchemy.dialects.postgresql as pg

db_metadata = sql.MetaData()

# This eventually could have the region and stuff on it so it's just not the id
connected_realms_table = sql.Table(
    "connected_realms",
    db_metadata,
    sql.Column("id", pg.INTEGER, primary_key=True),
    sql.Column("href", pg.TEXT),
    sql.Column("population", pg.TEXT),
    sql.Column("mythic_leaderboards_href", pg.TEXT),
    sql.Column("auctions_href", pg.TEXT),
    sql.Column("updated_at", pg.DATE),
)

realms_table = sql.Table(
    "realms",
    db_metadata,
    sql.Column("id", pg.INTEGER, primary_key=True),
    sql.Column("name", pg.TEXT),
    sql.Column("href", pg.TEXT),
    sql.Column("category", pg.TEXT),
    sql.Column("locale", pg.TEXT),
    sql.Column("timezone", pg.TEXT),
    sql.Column("type", pg.TEXT),
    sql.Column("slug", pg.TEXT),
    sql.Column("is_tournament", pg.BOOLEAN),
    sql.Column("connected_realm_id", pg.INTEGER),
    sql.Column("region_id", pg.INTEGER),
    sql.Column("updated_at", pg.DATE),
)

regions_table = sql.Table(
    "regions",
    db_metadata,
    sql.Column("id", pg.INTEGER, primary_key=True),
    sql.Column("name", pg.TEXT),
    sql.Column("href", pg.TEXT),
    sql.Column("updated_at", pg.DATE),
)

mythic_keystone_season = sql.Table(
    "mythic_keystone_seasons",
    db_metadata,
    sql.Column("id", pg.INTEGER, primary_key=True),
    sql.Column("start_timestamp", pg.TIMESTAMP),
    sql.Column("end_timestamp", pg.TIMESTAMP),
)

mythic_keystone_period_table = sql.Table(
    "mythic_keystone_periods",
    db_metadata,
    sql.Column("id", pg.INTEGER, primary_key=True),
    sql.Column("start_timestamp", pg.TIMESTAMP),
    sql.Column("end_timestamp", pg.TIMESTAMP),
    sql.Column("season_id", pg.INTEGER),
)

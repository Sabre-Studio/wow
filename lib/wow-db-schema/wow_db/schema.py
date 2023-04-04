import sqlalchemy as sql
import sqlalchemy.dialects.postgresql as pg

db_metadata = sql.MetaData()

# This eventually could have the region and stuff on it so it's just not the id
connected_realms_table = sql.Table(
    "connected_realms",
    db_metadata,
    sql.Column("id", pg.INTEGER, primary_key=True),
)

realms_table = sql.Table(
    "realms",
    db_metadata,
    sql.Column("id", pg.INTEGER, primary_key=True),
    sql.Column('name', pg.TEXT),
    sql.Column('connected_realm_id', pg.INTEGER),
)

# regions_table = sql.Table(
#     "regions", db_metadata, sql.Column("id", pg.INTEGER, primary_key=True)
# )


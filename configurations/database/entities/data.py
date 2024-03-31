import sqlalchemy


def dato(metadata):
    return sqlalchemy.Table(
        "data",
        metadata,
        sqlalchemy.Column("id", sqlalchemy.BIGINT, primary_key=True),
        sqlalchemy.Column("date", sqlalchemy.DATE),
        sqlalchemy.Column("time", sqlalchemy.TIME),
        sqlalchemy.Column("sensor", sqlalchemy.VARCHAR(255)),
        sqlalchemy.Column("type", sqlalchemy.VARCHAR(255)),
        sqlalchemy.Column("value", sqlalchemy.DOUBLE),
    )

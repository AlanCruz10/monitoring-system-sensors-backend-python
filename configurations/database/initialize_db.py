import databases
import databases.backends
import databases.backends.mysql
import sqlalchemy
from configurations.database.credentials.credential_database import DATABASE_URL
from configurations.database.entities.data import dato

entities_instance = None


def connecting_to_db():
    return databases.Database(DATABASE_URL)


def creating_metadata():
    print("Creating MetaData ...")
    metadata = sqlalchemy.MetaData()
    # Add entities to create tables in the database
    dato(metadata)
    engine = sqlalchemy.create_engine(DATABASE_URL)
    metadata.create_all(engine)
    get_instance_metadata(metadata=metadata)
    print("Metadata Created ...")


def get_instance_metadata(metadata):
    global entities_instance
    entities_instance = metadata
    return


def get_entities(entity):
    return entities_instance.tables[entity]

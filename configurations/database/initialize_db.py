import databases
import databases.backends
import databases.backends.mysql
import sqlalchemy
from configurations.database.entities.data import dato
from os import getenv
from dotenv import load_dotenv
from configurations.console.logger import logger

entities_instance = None

load_dotenv()


def connecting_to_db():
    return databases.Database(getenv('URL_DATABASE'))


def creating_metadata():
    logger.info("Creating MetaData ...")
    metadata = sqlalchemy.MetaData()
    # Add entities to create tables in the database
    dato(metadata)
    engine = sqlalchemy.create_engine(getenv('URL_DATABASE'))
    metadata.create_all(engine)
    get_instance_metadata(metadata=metadata)
    logger.info("Metadata Created ...")


def get_instance_metadata(metadata):
    global entities_instance
    entities_instance = metadata
    return


def get_entities(entity):
    return entities_instance.tables[entity]

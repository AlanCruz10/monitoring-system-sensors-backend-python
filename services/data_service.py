from configurations.database.initialize_db import connecting_to_db, get_entities
from datetime import datetime, time


async def save_data(data):
    date_now = datetime.now()
    for sensor, measures in data.items():
        for measurement, value in measures.items():
            db = connecting_to_db()
            await db.connect()
            await db.execute(
                get_entities(entity="data").insert().values(
                    date=date_now.date(),
                    time=time.fromisoformat(date_now.strftime("%H:%M:%S")),
                    type=measurement,
                    sensor=sensor,
                    value=value,
                )
            )
            await db.disconnect()

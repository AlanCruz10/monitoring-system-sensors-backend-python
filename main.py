from configurations.database.initialize_db import connecting_to_db, creating_metadata, get_entities
from configurations.firebase.routes.routes_firebase import routes
from datetime import datetime, time
import asyncio


async def main():
    creating_metadata()
    sensors = routes(route="sensors").get()

    for sensor, measures in sensors.items():
        for measurement, value in measures.items():
            db = connecting_to_db()
            await db.connect()
            await db.execute(
                get_entities(entity="data").insert().values(
                    date=datetime.now().date(),
                    time=time.fromisoformat(datetime.now().strftime("%H:%M:%S")),
                    type=measurement,
                    sensor=sensor,
                    value=value,
                )
            )
            await db.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

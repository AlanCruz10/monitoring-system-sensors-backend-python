from configurations.database.initialize_db import creating_metadata
from configurations.firebase.routes.routes_firebase import routes
from services.data_service import save_data
import asyncio


async def main():
    creating_metadata()
    time_saved = 0
    while True:
        sensors = routes(route="sensors").get()
        time_saved += 1
        if time_saved == 5:
            await save_data(data=sensors)
            time_saved = 0
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

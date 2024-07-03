from configurations.database.initialize_db import creating_metadata
from configurations.firebase.routes.routes_firebase import routes
from services.data_service import save_data
import asyncio
from configurations.console.logger import logger


async def main():
    try:
        logger.info("Starting sensor monitoring service")
        creating_metadata()
        time_saved = 0
        while True:
            try:
                sensors = routes(route="sensors").get()
                time_saved += 1
                if time_saved == 5:
                    await save_data(data=sensors)
                    time_saved = 0
                await asyncio.sleep(1)
            except Exception as e:
                logger.error(f"Error during execution: {str(e)}")
                await asyncio.sleep(5)

    except KeyboardInterrupt:
        logger.info("Stopped service")
    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
    finally:
        logger.info("Shutting down sensor monitoring service")


if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

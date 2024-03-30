from firebase_admin import db
from .. import initialize_firebase

initialize_firebase.initialize_firebase()

list_routes = {
    "dht11_humidity": db.reference("/sensor/dht11/humidity"),
    "dht11_temperature": db.reference("/sensor/dht11/temperature"),
    "ds18b20_temperature": db.reference("/sensor/ds18b20/temperature"),
    "sensors": db.reference("/sensor")
}


def routes(route):
    return list_routes[route]

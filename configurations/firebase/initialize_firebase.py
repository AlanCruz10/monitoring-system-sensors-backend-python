import firebase_admin
from firebase_admin import credentials
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def initialize_firebase():
    cred = credentials.Certificate(getenv('FIREBASE_CREDENTIAL_ROUTE'))
    initialize_app = firebase_admin.initialize_app(cred, {
        'databaseURL': getenv('FIREBASE_DB_REAL_TIME')})
    return initialize_app

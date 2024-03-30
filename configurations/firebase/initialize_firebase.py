import firebase_admin
from firebase_admin import credentials
import os


def initialize_firebase():
    # target = "configuration_firebase.json"
    # initial_dir = 'C:\\'
    # path = ''
    # for root, _, files in os.walk(initial_dir):
    #     if target in files:
    #         path = os.path.join(root, target)
    #         break
    cred = credentials.Certificate('configurations/firebase/credentials/configuration_firebase.json')
    initialize_app = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://monitoring-system-87637-default-rtdb.firebaseio.com/'})
    return initialize_app

from os import environ
from dotenv import load_dotenv

load_dotenv('.env')

class Config:
    API = environ.get('API')
    DB_PASS = environ.get('DB_PASS')
    DB_HOST = environ.get('DB_HOST')
    DB_USER= environ.get('DB_USER')
    DB_NAME= environ.get('DB_NAME')
    DB_AUTH= environ.get('DB_AUTH')
    WTF_CSRF_SECRET_KEY = 'a random string'
    SECRET_KEY = 'a random string'

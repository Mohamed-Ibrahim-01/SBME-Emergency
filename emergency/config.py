from os import environ


class Config:
    API = environ.get('API')
    DB_PASS = environ.get('DB_PASS')

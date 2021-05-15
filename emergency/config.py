from os import environ


class Config:
    API = environ.get('API')

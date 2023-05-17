import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = os.environ.get('DATABASE_URL')
    DEBUG = os.environ.get('DEBUG')

    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 4000
    SERVER_RELOAD = True


settings = Settings()

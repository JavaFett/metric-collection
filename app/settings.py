from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ''
    DEBUG: bool = True

    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 4000
    SERVER_RELOAD: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()

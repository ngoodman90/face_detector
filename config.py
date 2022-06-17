import pydantic


class Settings(pydantic.BaseSettings):
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()

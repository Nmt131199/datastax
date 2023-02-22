import os
from pydantic import BaseSettings, Field # come as default with fastapi
from functools import lru_cache

os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = '1'

class Settings(BaseSettings):
    aws_access_key_id: str = None
    aws_secret_access_key: str = None
    db_client_id: str = Field(..., env="ASTRA_DB_CLIENT_ID")
    db_client_secret: str = Field(..., env="ASTRA_DB_CLIENT_SECRET")

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()
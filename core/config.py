from typing import Any, Dict, List, Optional, Union
from pydantic_settings import BaseSettings, SettingsConfigDict

from pydantic import AnyHttpUrl, validator
from sqlalchemy.engine import create_engine


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")
    model_config['BACKEND_CORS_ORIGINS'] = []

    @validator('model_config.BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator('model_config.DATABASE_URL', pre=True)
    def assemble_database_url(cls, v, values):
        db_user = values.get('DB_USER')
        db_password = values.get('DB_PASSWORD')
        db_host = values.get('DB_HOST')
        db_port = values.get('DB_PORT')
        db_name = values.get('DB_NAME')
        return DATABASE_URL


settings = Settings()

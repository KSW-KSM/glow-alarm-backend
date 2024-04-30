from typing import Any, Dict, List, Optional, Union
from pydantic_settings import BaseSettings, SettingsConfigDict

from pydantic import AnyHttpUrl, validator
from sqlalchemy.engine import create_engine


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")
    
settings = Settings()

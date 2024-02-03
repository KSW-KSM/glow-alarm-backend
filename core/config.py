from typing import Any, Dict, List, Optional, Union
from pydantic_settings import BaseSettings

from pydantic import AnyHttpUrl, validator
from sqlalchemy.engine import create_engine


class Settings(BaseSettings):
    PROJECT_NAME: str = 'SoundLight'
    API_VERSION: str = 'v1'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    DESCRIPTION: str = '프로젝트 soundlight의 api 문서입니다.'
    DB_USER: str = 'root'
    DB_PASSWORD: str = 'soundlight1234%21%40' # soundlight1234!@과 동일 - 연결자 중복 이슈로 변경
    DB_HOST: str = 'localhost'
    DB_PORT: int = 3306
    DB_NAME: str = 'soundlight'
    DATABASE_URL: Optional[str] = None

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator('DATABASE_URL', pre=True)
    def assemble_database_url(cls, v, values):
        db_user = values.get('DB_USER')
        db_password = values.get('DB_PASSWORD')
        db_host = values.get('DB_HOST')
        db_port = values.get('DB_PORT')
        db_name = values.get('DB_NAME')
        if not all([db_user, db_password, db_host, db_port, db_name]):
            raise ValueError('Missing database connection information')
        url = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        return url


settings = Settings()

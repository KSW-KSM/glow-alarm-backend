from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings

# Create the SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for the ORM models
Base = declarative_base()

from models.test_item import TestItem
from models.alarm import Alarm
from models.user import User
# from models.disaster import Disaster


Base.metadata.create_all(bind=engine)

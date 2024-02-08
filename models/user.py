from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class User(Base, TimeStampedModel):
    __tablename__ = "test_item"

    id = Column(String(20), primary_key=True, index=True)
    user_name = Column(String(20), nullable=False)
    google_id = Column(String(20), nullable=False)
    guardian_contact = Column(String(20), nullable=False)
    bulb_connection = Column(Boolean, nullable=False, default=False)
    bulb_ip = Column(String(20))
    value = Column(Integer)
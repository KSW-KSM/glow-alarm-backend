from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

import uuid

class User(Base, TimeStampedModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(20), nullable=False)
    google_id = Column(String(20), nullable=False)
    guardian_contact = Column(String(20), nullable=False)
    bulb_connection = Column(Boolean, nullable=False, default=False)
    bulb_ip = Column(String(20))
    location_id = Column(Integer, ForeignKey('location.id'))

    location = relationship("Location", back_populates="users")
    alarms = relationship("Alarm", back_populates="user")
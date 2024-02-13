from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

import uuid

class User(Base, TimeStampedModel):
    __tablename__ = "user"

    id = Column(String(20), primary_key=True, index=True, default=str(uuid.uuid4()))
    user_name = Column(String(20), nullable=False)
    google_id = Column(String(20), nullable=False)
    guardian_contact = Column(String(20), nullable=False)
    bulb_connection = Column(Boolean, nullable=False, default=False)
    bulb_ip = Column(String(20))

    alarms = relationship("Alarm", back_populates="user")
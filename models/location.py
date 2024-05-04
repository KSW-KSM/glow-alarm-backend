from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import uuid

class Location(Base, TimeStampedModel):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    location_code = Column(String(40), nullable=False)
    location_name = Column(String(20), nullable=False)

    users = relationship("User", back_populates="location")
    disasters = relationship("Disaster", back_populates="location")
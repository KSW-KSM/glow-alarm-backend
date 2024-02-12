from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, Long, String
from sqlalchemy.orm import relationship

class Location(Base, TimeStampedModel):
    __tablename__ = "location"

    id = Column(String(20), primary_key=True, index=True)
    location_code = Column(Long(20), nullable=False)
    location_name = Column(String(20), nullable=False)
    user = relationship("User", back_populates="location")
    disaster = relationship("Disaster", back_populates="location")
from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Long, Column, Integer, String, Boolean, DateTime ,ForeignKey
from sqlalchemy.orm import relationship


class DisasterInfo(Base, TimeStampedModel):
    __tablename__ = "disasterInfo"
    
    id = Column(String(20), primary_key=True, index=True)
    disaster_time = Column(Long(20), nullable=False)
    disaster_level = Column(String(20), nullable=False)
    disaster_message = Column(String(20), nullable=False)
    location_id = Column(String(20), ForeignKey('location.id'))
    locationInfo = relationship("LocationInfo", back_populates="disasterInfo")
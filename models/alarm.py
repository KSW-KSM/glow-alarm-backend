from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy_enum import EnumType
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum

class WeekdayEnum(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
class LightColor(Enum):
    RED = "Red"

class Alarm(Base, TimeStampedModel):
    __tablename__ = "alarm"

    id = Column(String(20), primary_key=True, index=True)
    alarm_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    repeat_day = Column(EnumType(WeekdayEnum, create_constraint=False), nullable=True)
    light_color= Column(EnumType(LightColor, create_constraint=False), nullable = False, default = LightColor.RED)
    alarm_status = Column(Column(Boolean, nullable=False, default=False))

    user_id = Column(String(20), ForeignKey('user.id'))
    user = relationship("User", back_populates="alarms")
from db.base import Base
from models.columns.timestamp import TimeStampedModel
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime

class WeekdayEnum(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class LightColor(str, Enum):
    RED = "Red"

class Alarm(Base, TimeStampedModel):
    __tablename__ = "alarm"

    id = Column(String(20), primary_key=True, index=True)
    alarm_time = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    repeat_day = Column(Enum(WeekdayEnum))
    light_color= Column(Enum(LightColor),  default = LightColor.RED)
    alarm_status = Column(Column(Boolean,  default=False))
    user_id = Column(String(20), ForeignKey('user.id'))
    user = relationship("User", back_populates="alarms")
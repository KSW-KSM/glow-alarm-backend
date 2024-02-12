from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AlarmBase(BaseModel):
    id: str
    alarm_time: datetime
    repeat_day: str
    light_color: str
    alarm_status: bool
    user_id: str


class AlarmCreate(AlarmBase):
    pass


class AlarmUpdate(AlarmBase):
    pass


class AlarmInDB(AlarmBase):
    class Config:
        orm_mode = True

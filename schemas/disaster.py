from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DisasterBase(BaseModel):
    disaster_time: datetime
    disaster_level: str
    disaster_message: str
    location_id: int

class DisasterCreate(DisasterBase):
    pass


class DisasterUpdate(DisasterBase):
    pass

class DisasterResponse(DisasterBase):
    id: int
    pass

class DisasterInDB(DisasterBase):
    class Config:
        orm_mode = True


from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class LocationBase(BaseModel):
    
    id: str
    location_code: str
    location_name: str


class LocationCreate(LocationBase):
    pass


class LocationUpdate(LocationBase):
    pass


class LocationInDB(LocationBase):
    class Config:
        orm_mode = True


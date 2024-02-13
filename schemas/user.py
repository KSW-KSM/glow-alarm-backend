from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    user_name: str
    google_id: str
    guardian_contact: str
    bulb_ip: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    bulb_connection: bool
    pass


class UserInDB(UserBase):
    class Config:
        orm_mode = True

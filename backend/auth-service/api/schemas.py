from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    name: str
    surname: str
    class Config:
        orm_mode = True
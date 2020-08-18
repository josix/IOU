from datetime import datetime

from pydantic import BaseModel


class GroupBase(BaseModel):
    line_id: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    line_id: str
    display_name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class UserGroupBase(BaseModel):
    user_id: int
    group_id: int


class UserGroup(UserGroupBase):
    id: int
    user_id: int
    group_id: int
    activated_time: datetime


class UserGroupCreate(UserGroupBase):
    pass

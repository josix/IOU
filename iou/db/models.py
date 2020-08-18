import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class UserGroup(Base):
    __tablename__ = "user_group"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    activated_time = Column(DateTime, default=datetime.datetime.utcnow)

    # TODO: complete relationship table
    # user = relationship("User", back_populates="groups")
    # group = relationship("Group", back_populates="users")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    line_id = Column(String, unique=True, index=True)
    display_name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    # groups = relationship("UserGroup", back_populates="user")


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    line_id = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

    # users = relationship("UserGroup", back_populates="user")

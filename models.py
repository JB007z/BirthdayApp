
from sqlalchemy import Boolean,Column,ForeignKey,Integer,String,Enum,Table,DateTime,UniqueConstraint,Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db import Base
import enum



#user
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)

#group
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer,index=True,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"),index=True)
    name = Column(String)

#bday
class Birthday(Base):
    __tablename__ = "birthdays"
    id = Column(Integer,index=True,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"),index=True)
    group_id  = Column(Integer,ForeignKey("groups.id"),nullable=True,index=True)
    date = Column(Date)
    full_name = Column(String)
    description = Column(String)
    photo_url = Column(String)

class ShareLEvel(String,enum.Enum):
    FULL = "full_share"
    PARTIAL = "partial_share"

#birthday share
class BirthdayShare(Base):
    __tablename__ = "birthday_share"
    id = Column(Integer,primary_key=True,index=True)
    birthday_id = Column(Integer,ForeignKey("birthdays.id"),index=True)
    shared_with_user_id = Column(Integer,ForeignKey("users.id"),index=True)
    share_level = Column(
        Enum(ShareLEvel,name="share_enum"),
        nullable=False
    )


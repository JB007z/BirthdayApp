import os
import models,db
from sqlalchemy import String
from dotenv import load_dotenv
from datetime import datetime,timedelta
from typing import Optional
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_EXPIRES = 60*24

#create_hash
password_context = CryptContext(schemes=["argon2"],deprecated="auto")
def create_hash(password:String):
   return password_context.hash(password)

def verify_hash(plain_password:String,hash:String):
   return password_context.verify(plain_password,hash)



#verify_hash


#create_access_token


#get_current_user

import os
import models,db
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from repository.user_repo import UserRepository
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_EXPIRES = 60*24

#create_hash
password_context = CryptContext(schemes=["argon2"],deprecated="auto")
def create_hash(password:str):
   return password_context.hash(password)

def verify_hash(plain_password:str,hashed_password:str):
   return password_context.verify(plain_password,hashed_password)

#create_access_token
def create_access_token(user_id:int):
   expire = datetime.now(timezone.utc) + timedelta(minutes=30)
   payload = {
      "sub":str(user_id),
      "exp":expire
   }

   token = jwt.encode(
      payload,
      SECRET_KEY,
      algorithm=ALGORITHM
   )
   return token


#get_current_user
async def get_current_user(
   token:str = Depends(oauth2_scheme),
   db:AsyncSession = Depends(db.get_db)
   ):
   credentials_exception =  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate the credentials",headers={"WWW-Authenticate": "Bearer"})
   
   try:
      payload = jwt.decode(
         token,
         SECRET_KEY,
         algorithms=[ALGORITHM]
      )
      user_id = int(payload.get("sub"))
      if user_id is None:
         raise credentials_exception
   except JWTError:
      raise credentials_exception
   
   user_repository = UserRepository(db)
   user = await user_repository.get_by_id(user_id)
   if  user is None:
      raise credentials_exception
   
   return user 
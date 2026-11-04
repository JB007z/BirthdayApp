from models import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    def get_by_id(self,user_id:int):
        return self.db.query(User).filter(User.id == user_id).first()

    
    def get_by_email(self,user_email:str):
        return self.db.query(User).filter(User.email == user_email).first
    
    def create(self,user:User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def delete(self,user_id:int):
        user = get_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
    
    def update(self,user:User):
        self.db.commit()
        self.db.refresh(user)

        return user

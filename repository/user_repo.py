from models import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    async def get_by_id(self,user_id:int):
        result = await self.db.query(User).filter(User.id == user_id).first()
        return result
    
    async def get_by_email(self,user_email:str):
        result = await self.db.query(User).filter(User.email == user_email).first
        return result
        
    async def create(self,user:User):
        await self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    
    async def delete(self,user_id:int):
        user = get_by_id(user_id)
        if user:
            await self.db.delete(user)
            await self.db.commit()
    
    async def update(self,user:User):
        await self.db.commit()
        await self.db.refresh(user)

        return user

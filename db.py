from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncSession
from sqlalchemy.orm import declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url,echo=True)
AssyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
Base = declarative_base()


async def get_db():
    async with AssyncSessionLocal() as session:
        yield session
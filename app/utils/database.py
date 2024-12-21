import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import app.models

load_dotenv()

db_url = os.getenv("Database_url")

engine = create_async_engine(db_url)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with async_session() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(app.models.Base.metadata.create_all)
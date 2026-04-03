from sqlmodel import create_engine, SQLModel
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine

from src.config import Config

async_engine = AsyncEngine(
    create_engine(
    url = Config.DATABASE_URL,
    echo=True
))

async def init_db():
    async with async_engine.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)
    # async with async_engine.begin() as conn:
    #     statement = text("SELECT 'hello';")
    #     result = await conn.execute(statement)
    #     print(result.all())

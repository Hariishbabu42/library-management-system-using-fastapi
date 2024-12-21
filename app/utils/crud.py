from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Books
from app.schemas import *

async def new_book(db: AsyncSession, book_data: RegisterBooks):
    new_book = Books(**book_data.dict())
    db.add(new_book)
    await db.commit()
    await db.refresh(new_book)
    return new_book

async def get_books(db: AsyncSession):
    books = await db.execute(select(Books))
    return books

async def get_book(db: AsyncSession, book_id: int):
    book = await db.get(Books, book_id)
    return book

async def update_book(db: AsyncSession, book_id: int, book_data: RegisterBooks):
    book = await db.get(Books, book_id)
    if book:
        for key, value in book_data.dict().items():
            setattr(book, key, value)
        await db.commit()
    return book

async def delete_book(db: AsyncSession, book_id: int):
    book = await db.get(Books, book_id)
    if book:
        await db.delete(book_id)
        await db.commit()
    return book
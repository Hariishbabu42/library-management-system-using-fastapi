from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import *
from utils.database import get_db
from utils.crud import *

books_router = APIRouter(prefix="/library", tags=["Books"])
user_router = APIRouter(prefix="/library",  tags=["Users"])


@books_router.post("/register_new_book", response_model=BooksResponse)
async def register_book(book_data : RegisterBooks, db : AsyncSession = Depends(get_db)):
    book = await new_book(db, book_data)
    return book
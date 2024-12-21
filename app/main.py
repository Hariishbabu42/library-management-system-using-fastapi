from fastapi import FastAPI

from app.routers import library
from utils.database import init_db

app = FastAPI(title = "Library Management")

app.include_router(library.books_router)

@app.lifespan("startup")
async def on_startup():
    await init_db()
    
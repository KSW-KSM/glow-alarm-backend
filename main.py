from fastapi import FastAPI
from api.router import api_router
from core.config import settings
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import text
from api.depends.get_db import get_db
import asyncio
import logging

# from models.create_table import init_table
from routers import users, posts

app = app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.API_VERSION
)

app.include_router(api_router)



#### add CORS middleware ####
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#### checking db connection ####
def check_db_connection(db=None):
    if not db:
        gen = get_db()
        db = next(gen)
        try:
            db.execute(text("SELECT 1"))
        finally:
            next(gen, None)
    else:
        db.execute(text("SELECT 1"))


async def startup_db_check():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, check_db_connection)


@app.on_event("startup")
async def on_startup():
    logging.info("Trying DB connection before stating...")
    await startup_db_check()
    logging.info(f"DB connected! (url: {settings.DATABASE_URL})")

# Initialize table
# init_table()

# app.include_router(users.router)
# app.include_router(posts.router)

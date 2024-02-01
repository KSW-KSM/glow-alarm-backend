from fastapi import FastAPI

# from models.create_table import init_table
from routers import users, posts

app = app = FastAPI(
    title="soundlight api",
    description="This is a sample FastAPI application with Swagger documentation.",
    version="1.0.0",
    openapi_url="/openapi.json",  # JSON 형식의 API 스키마
)

# Initialize table
# init_table()

# app.include_router(users.router)
# app.include_router(posts.router)

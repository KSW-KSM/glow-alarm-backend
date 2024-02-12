from fastapi import APIRouter
from api.routes import test_item, user, alarm

api_router = APIRouter()

api_router.include_router(test_item.router, tags=["test_item"])
api_router.include_router(user.router, tags = ['유저'])
api_router.include_router(alarm.router, tags = ['알람'])
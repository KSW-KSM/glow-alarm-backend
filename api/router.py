from fastapi import APIRouter
from api.routes import test_item, user

api_router = APIRouter()

api_router.include_router(test_item.router, tags=["test_item"])
api_router.include_router(user.router, tags = ['user'])
# api_router.include_router(system_config.router, tags=["시스템 환경 설정"])
# api_router.include_router(travel_share_info.router, tags=["여행 일정 공유 관리"])
# api_router.include_router(travel_default_info.router, tags=["여행 기본 정보 관리"])
# api_router.include_router(travel_flight_add_info.router, tags=["여행 추가 정보(항공편) 관리"])
# api_router.include_router(travel_add_info.router, tags=["여행 추가 정보(숙박, 음식점, 관광지) 관리"])
# api_router.include_router(travel_schedule_info.router, tags=["여행 추천 일정 관리"])
# api_router.include_router(travel_review_info.router, tags=["여행 리뷰 관리"])
# api_router.include_router(travel_review_file_info.router, tags=["travel_review_file_info"])
# api_router.include_router(log_manage.router, tags=["로그 관리"])

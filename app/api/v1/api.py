from fastapi import APIRouter

from app.api.v1.endpoints import investment

api_router = APIRouter()
api_router.include_router(investment.router, prefix="/investment", tags=["investment"])
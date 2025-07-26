from typing import List
from fastapi import APIRouter, HTTPException
from app.schemas.investment import InvestmentRequest,InvestmentResponse
router = APIRouter()


@router.post("/", response_model=InvestmentResponse)
async def create_user(user: InvestmentRequest):
    return ""

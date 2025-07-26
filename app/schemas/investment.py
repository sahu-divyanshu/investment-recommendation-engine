from pydantic import BaseModel, EmailStr
from typing import Optional


class InvestmentRequest(BaseModel):
    name: str



class InvestmentResponse(BaseModel):
    name:str


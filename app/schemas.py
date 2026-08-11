from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: Optional[str] = None


class LeadBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    empresa: str = Field(min_length=1, max_length=120)
    email: EmailStr
    telefone: str = Field(min_length=8, max_length=30)
    status: bool = True
    pontuacao: int = Field(default=0, ge=0, le=100)
    observacoes: str = ""


class LeadCreate(LeadBase):
    pass


class LeadUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=120)
    empresa: Optional[str] = Field(default=None, min_length=1, max_length=120)
    email: Optional[EmailStr] = None
    telefone: Optional[str] = Field(default=None, min_length=8, max_length=30)
    status: Optional[bool] = None
    pontuacao: Optional[int] = Field(default=None, ge=0, le=100)
    observacoes: Optional[str] = None


class LeadOut(LeadBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = {"from_attributes": True}

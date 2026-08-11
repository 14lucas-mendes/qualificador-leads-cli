from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import User
from app.schemas import LeadCreate, LeadOut, LeadUpdate
from app.services import create_lead, delete_lead, get_lead, list_leads, update_lead

router = APIRouter(prefix="/leads", tags=["leads"])


@router.post("", response_model=LeadOut, status_code=status.HTTP_201_CREATED)
def create(
    lead_in: LeadCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_lead(db, lead_in, current_user.id)


@router.get("", response_model=list[LeadOut])
def list_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_leads(db, current_user.id)


@router.get("/{lead_id}", response_model=LeadOut)
def get_one(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    lead = get_lead(db, lead_id, current_user.id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead não encontrado")
    return lead


@router.patch("/{lead_id}", response_model=LeadOut)
def patch(
    lead_id: int,
    lead_in: LeadUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    lead = get_lead(db, lead_id, current_user.id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead não encontrado")
    return update_lead(db, lead, lead_in)


@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    lead = get_lead(db, lead_id, current_user.id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead não encontrado")
    delete_lead(db, lead)

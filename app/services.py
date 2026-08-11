from sqlalchemy.orm import Session

from app.models import Lead
from app.schemas import LeadCreate, LeadUpdate


def create_lead(db: Session, lead_in: LeadCreate, owner_id: int) -> Lead:
    lead = Lead(**lead_in.model_dump(), owner_id=owner_id)
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead


def list_leads(db: Session, owner_id: int) -> list[Lead]:
    return db.query(Lead).filter(Lead.owner_id == owner_id).order_by(Lead.id.desc()).all()


def get_lead(db: Session, lead_id: int, owner_id: int) -> Lead | None:
    return (
        db.query(Lead)
        .filter(Lead.id == lead_id, Lead.owner_id == owner_id)
        .first()
    )


def update_lead(db: Session, lead: Lead, lead_in: LeadUpdate) -> Lead:
    data = lead_in.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(lead, field, value)
    db.commit()
    db.refresh(lead)
    return lead


def delete_lead(db: Session, lead: Lead) -> None:
    db.delete(lead)
    db.commit()

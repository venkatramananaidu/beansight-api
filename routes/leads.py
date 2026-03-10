from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Lead
from schemas import LeadCreate, LeadResponse

router = APIRouter()

@router.post("/submit-interest", response_model=LeadResponse)
def submit_interest(lead: LeadCreate, db: Session = Depends(get_db)):
    try:
        db_lead = Lead(
            email=lead.email,
            forecast_method=lead.forecast_method,
            staff_count=lead.staff_count,
            pos_system=lead.pos_system,
            challenges=lead.challenges,
            features_interest=lead.features_interest,
            willingness_to_pay=lead.willingness_to_pay,
        )
        db.add(db_lead)
        db.commit()
        db.refresh(db_lead)
        return db_lead
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/leads")
def get_leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).order_by(Lead.created_at.desc()).all()
    return leads
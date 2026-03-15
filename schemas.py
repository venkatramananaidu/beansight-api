from pydantic import BaseModel
from typing import List, Optional

class LeadCreate(BaseModel):
    email: Optional[str] = None
    forecast_method: Optional[str] = None
    staff_count: Optional[str] = None
    pos_system: Optional[str] = None
    challenges: Optional[List[str]] = []
    features_interest: Optional[List[str]] = []
    willingness_to_pay: Optional[str] = None

class LeadResponse(BaseModel):
    id: int
    email: Optional[str]
    status: str

    class Config:
        from_attributes = True


class SubscriberCreate(BaseModel):
    email: str
    source: Optional[str] = None

class SubscriberResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True
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
```

---

**requirements.txt**
```
fastapi==0.110.0
uvicorn==0.29.0
sqlalchemy==2.0.29
psycopg2-binary==2.9.9
pydantic==2.6.4
python-dotenv==1.0.1
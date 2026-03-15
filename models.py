from sqlalchemy import Column, Integer, String, ARRAY, DateTime
from sqlalchemy.sql import func
from database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=True)
    forecast_method = Column(String, nullable=True)
    staff_count = Column(String, nullable=True)
    pos_system = Column(String, nullable=True)
    challenges = Column(ARRAY(String), nullable=True)
    features_interest = Column(ARRAY(String), nullable=True)
    willingness_to_pay = Column(String, nullable=True)
    status = Column(String, default="new")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    source = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
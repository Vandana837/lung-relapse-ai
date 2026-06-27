from sqlalchemy import Column, Integer, String

from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True, index=True)
    full_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    smoking_history = Column(String)
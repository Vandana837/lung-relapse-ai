from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.patient import Patient
from app.schemas.patient_schema import PatientCreate

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = Patient(
        patient_id=patient.patient_id,
        full_name=patient.full_name,
        age=patient.age,
        gender=patient.gender,
        smoking_history=patient.smoking_history
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient added successfully",
        "patient": new_patient
    }


@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()
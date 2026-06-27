from pydantic import BaseModel


class PatientCreate(BaseModel):
    patient_id: str
    full_name: str
    age: int
    gender: str
    smoking_history: str


class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True
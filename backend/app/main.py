from fastapi import FastAPI
from app.database import Base, engine
from app.models.patient import Patient
from app.routes.patient_routes import router as patient_router

app = FastAPI(
    title="Lung Relapse AI API",
    description="Backend API for Lung Cancer Relapse Prediction",
    version="1.0.0"
)
app.include_router(patient_router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to Lung Relapse AI Backend"
    }

@app.get("/health")
def health():
    return {
        "status": "Backend is running successfully"
    }


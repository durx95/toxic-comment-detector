from fastapi import APIRouter
from pydantic import BaseModel
from app.services.prediction_service import PredictionService
from app.db.mongodb import collection

router = APIRouter()
service = PredictionService()

class TextInput(BaseModel):
    text: str

@router.post("/predict")
def predict(data: TextInput):
    result = service.predict(data.text)

    # Save to DB
    collection.insert_one({
        "text": data.text,
        "prediction": result
    })

    return {"prediction": result}
from fastapi import FastAPI, HTTPException
from schemas import IncomePredictionRequest
from model.predictor import predict_income


app = FastAPI(title="Income Prediction API")

@app.get("/")
def home():
    return {"message": "route to predict endpoint to see prediction"}

@app.post("/predict")
def predict_adult_income(request_data: IncomePredictionRequest):
    try:
        prediction = predict_income(request_data)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

import os

port = int(os.environ.get("PORT", 7860))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
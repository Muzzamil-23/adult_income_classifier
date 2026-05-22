import os
import joblib
import pandas as pd
from schemas import IncomePredictionRequest


pipeline = None

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')

try:
    pipeline = joblib.load(model_path)
    print("Model loaded successfully!")
except FileNotFoundError:
    print(f"CRITICAL ERROR: Model file not found at {model_path}.")
except Exception as e:
    print(f"CRITICAL ERROR: Could not load model: {e}")


def predict_income(request_data: IncomePredictionRequest) -> str:
    if pipeline is None: 
        raise RuntimeError("The prediction model failed to load at startup.")

    data_dict = request_data.model_dump(by_alias=True)
    df = pd.DataFrame([data_dict])
    
    prediction = pipeline.predict(df)[0]
    return str(prediction)
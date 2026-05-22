# Adult Income Classifier

## Overview

This repository contains a full-stack machine learning project that predicts whether an individual earns more than $50K per year based on the UCI Adult Census dataset. The project includes:

- A **FastAPI** backend serving a serialized ML model
- A **Streamlit** frontend for interactive income prediction
- A Jupyter notebook for data exploration, model development, and evaluation
- A Dockerfile for containerizing the backend

The backend loads a pre-trained model from `backend/app/model/model.pkl`, accepts structured adult census features, and returns a binary income prediction.

## Repository Structure

```
adult_income_classifier/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── schemas.py
│       └── model/
│           ├── predictor.py
│           └── model.pkl
├── dataset/
│   └── adult.csv
├── frontend/
│   ├── app.py
│   └── requirements.txt
├── notebook/
│   └── Adult_income.ipynb
└── readme.md
```

## Machine Learning Models

The training notebook explores and evaluates four classification models using Scikit-learn pipelines. Each model uses a preprocessing pipeline that handles numeric and categorical features.

- **Logistic Regression**
  - A linear model for binary classification.
  - Serves as a baseline model and helps measure how well a linear decision boundary performs.

- **Decision Tree**
  - A tree-based model that captures non-linear feature interactions.
  - Useful for interpretability and for learning simple rules from categorical and numeric features.

- **Support Vector Classifier (SVC)**
  - A robust model that finds an optimal margin between income classes.
  - In the notebook evaluation, SVC achieved the highest accuracy at approximately **86.17%**.

- **K-Nearest Neighbors (KNN)**
  - A non-parametric method that predicts class based on nearest neighbors.
  - Good for capturing local structure in the feature space.

The current backend loads a serialized `model.pkl` pipeline, which is the trained model used for prediction.

## Tech Stack

- **FastAPI** - REST API backend
- **Uvicorn** - ASGI server for FastAPI
- **Pydantic** - request validation and schema enforcement
- **Streamlit** - interactive web UI
- **Scikit-learn** - model training and prediction
- **Pandas / NumPy** - data processing
- **joblib** - model serialization
- **Docker** - backend containerization

## Backend Details

### Key files

- `backend/app/main.py` - FastAPI application and endpoint definitions
- `backend/app/schemas.py` - Pydantic model for prediction request validation
- `backend/app/model/predictor.py` - loads `model.pkl` and performs inference
- `backend/Dockerfile` - container build instructions

### Input schema

The backend expects a JSON payload with the following fields:

- `age` (int)
- `workclass` (string)
- `fnlwgt` (int)
- `education` (string)
- `educational-num` (int)
- `marital-status` (string)
- `occupation` (string)
- `relationship` (string)
- `race` (string)
- `gender` (string)
- `capital-gain` (int)
- `capital-loss` (int)
- `hours-per-week` (int)
- `native-country` (string)

## Running Locally

### Backend

1. Open a terminal and navigate to the backend folder:

```powershell
cd d:\Smit\Assignments\adult_income_classifier\backend
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Start the FastAPI app:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 7860
```

The backend will be available at `http://localhost:7860`.

### Frontend

1. Open a second terminal and navigate to the frontend folder:

```powershell
cd d:\Smit\Assignments\adult_income_classifier\frontend
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Configure the backend URL. Create a `.env` file in `frontend/` with:

```text
API_URL=http://localhost:7860/predict
```

5. Run Streamlit:

```powershell
streamlit run app.py
```

The frontend will typically open at `http://localhost:8501`.

## API Endpoints

### `GET /`

Returns a basic status message:

```json
{
  "message": "route to predict endpoint to see prediction"
}
```

### `POST /predict`

Send a JSON object matching the `IncomePredictionRequest` schema.

Example request:

```bash
curl -X POST http://localhost:7860/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "workclass": "Private",
    "fnlwgt": 200000,
    "education": "Bachelors",
    "educational-num": 13,
    "marital-status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "gender": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 45,
    "native-country": "United-States"
  }'
```

Example response:

```json
{
  "prediction": "1"
}
```

- `0` indicates income `<= 50K`
- `1` indicates income `> 50K`

## Deployment

### Docker (backend)

Build the backend image:

```powershell
cd d:\Smit\Assignments\adult_income_classifier\backend
docker build -t adult-income-backend .
```

Run the container:

```powershell
docker run -p 7860:7860 adult-income-backend
```

### Notes

- The repository does not currently include a published public deployment URL.
- Use the Docker setup above or host the backend and Streamlit app on your preferred cloud service.

## Notebook and Model Development

- `notebook/Adult_income.ipynb` contains the full model development workflow.
- The notebook builds preprocessing pipelines and evaluates the four classifiers listed above.
- Evaluation output shows the models achieved roughly:
  - Logistic Regression: 85.74%
  - Decision Tree: 81.96%
  - SVC: 86.17%
  - KNN: 84.01%

## Additional Information

- Keep `backend/app/model/model.pkl` present for inference to work.
- The frontend maps user-friendly labels to the backend feature values required by the model.
- If you update the trained model, re-export the serialized pipeline to `model.pkl`.

---

### Contact

For questions or improvements, update the notebook and backend pipeline, then verify predictions using the Streamlit UI.

import joblib
import pandas as pd

# Load model
model = joblib.load("models/fraud_model.pkl")

def predict_transaction(data):

    input_data = pd.DataFrame([data])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    return prediction, probability
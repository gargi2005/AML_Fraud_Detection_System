import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from preprocessing import preprocess_data


# Load Dataset
df = pd.read_csv("data/TFL - FINAL-1.csv")

# Preprocess Dataset
df = preprocess_data(df)

# Features and Target
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

# Encoding
X = pd.get_dummies(X, drop_first=True)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight='balanced'
)

# Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Metrics
print("\nModel Performance\n")

print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, "models/fraud_model.pkl")

# Save Columns
joblib.dump(
    X.columns.tolist(),
    "models/model_columns.pkl"
)

print("\nModel Saved Successfully")
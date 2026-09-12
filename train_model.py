import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Read the transaction dataset
data = pd.read_csv("dataset/transactions.csv")

# Use descriptions as input and categories as output
X = data["description"]
y = data["category"]

# Create and train the ML model
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(X, y)

# Create the model folder if it does not exist
os.makedirs("model", exist_ok=True)

# Save the trained model
joblib.dump(model, "model/expense_model.pkl")

print("Model trained and saved successfully!")
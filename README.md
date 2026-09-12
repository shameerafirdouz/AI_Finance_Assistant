# AI Finance Assistant

AI Finance Assistant is a beginner-friendly Flask web application that uses machine learning to predict the category of an expense from a transaction description.

## Features

- Predicts expense categories from transaction descriptions
- Uses a machine learning model
- Simple Flask web interface
- Supports categories such as Food, Transport, Entertainment, Health, Shopping, Bills, and more

## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn
- Joblib
- HTML and CSS

## Project Structure

```text
AI_Finance_Assistant
│
├── dataset
│   └── transactions.csv
├── model
│   └── expense_model.pkl
├── static
│   └── style.css
├── templates
│   └── index.html
│
├── app.py
├── train_model.py
└── requirements.txt

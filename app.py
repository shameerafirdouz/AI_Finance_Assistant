from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model/expense_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    description = ""

    if request.method == "POST":
        description = request.form["description"]
        prediction = model.predict([description])[0]

    return render_template(
        "index.html",
        prediction=prediction,
        description=description
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
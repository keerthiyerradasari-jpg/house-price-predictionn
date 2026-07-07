from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    area_type = int(request.form["area_type"])
    availability = int(request.form["availability"])
    location = int(request.form["location"])
    bhk = int(request.form["bhk"])
    total_sqft = float(request.form["total_sqft"])
    bath = int(request.form["bath"])
    balcony = int(request.form["balcony"])

    data = np.array([[area_type, availability, location,
                      bhk, total_sqft, bath, balcony]])

    prediction = model.predict(data)

    return render_template(
        "index.html",
        prediction_text=f"Predicted House Price: {prediction[0]:.2f} Lakhs"
    )

if __name__ == "__main__":
    app.run(debug=True)
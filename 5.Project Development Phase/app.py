from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# ==========================
# Load Model
# ==========================

model = joblib.load("model/hdi_model.pkl")


# ==========================
# HDI Category
# ==========================

def get_category(hdi):

    if hdi < 0.55:
        return "Low Human Development"

    elif hdi < 0.70:
        return "Medium Human Development"

    elif hdi < 0.80:
        return "High Human Development"

    else:
        return "Very High Human Development"


# ==========================
# Dashboard
# ==========================

@app.route("/")
def home():

    return render_template(
        "dashboard.html",
        prediction=None,
        pred_percent=0
    )


# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    life = float(request.form["life"])
    school_exp = float(request.form["school_exp"])
    school_mean = float(request.form["school_mean"])
    gni = float(request.form["gni"])

    features = [[

        life,
        school_exp,
        school_mean,
        gni

    ]]

    prediction = float(model.predict(features)[0])

    prediction = round(prediction, 3)

    category = get_category(prediction)

    pred_percent = round(prediction * 100, 1)

    # Simple AI Insight
    if prediction >= 0.80:

        insight = "Excellent overall human development with strong socio-economic indicators."

    elif prediction >= 0.70:

        insight = "Good development. Improvements in education or income can further increase HDI."

    elif prediction >= 0.55:

        insight = "Moderate development. Better healthcare and education can improve well-being."

    else:

        insight = "Low development. Significant improvements are needed across health, education and income."

    return render_template(

        "dashboard.html",

        prediction=prediction,

        pred_percent=pred_percent,

        category=category,

        insight=insight,

        life=life,

        school_exp=school_exp,

        school_mean=school_mean,

        gni=gni

    )


if __name__ == "__main__":
    app.run(debug=True)
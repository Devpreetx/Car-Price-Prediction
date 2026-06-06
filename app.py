from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("car_price_model.pkl")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/guide")
def guide():
    return render_template("guide.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        try:

            enginesize  = float(request.form["enginesize"])
            curbweight  = float(request.form["curbweight"])
            horsepower  = float(request.form["horsepower"])
            carwidth    = float(request.form["carwidth"])
            carlength   = float(request.form["carlength"])
            drivewheel  = int(request.form["drivewheel"])
            wheelbase   = float(request.form["wheelbase"])
            boreratio   = float(request.form["boreratio"])
            fuelsystem  = int(request.form["fuelsystem"])
            citympg     = int(request.form["citympg"])
            highwaympg  = int(request.form["highwaympg"])

            sample = pd.DataFrame([{
                "enginesize":  enginesize,
                "curbweight":  curbweight,
                "horsepower":  horsepower,
                "carwidth":    carwidth,
                "carlength":   carlength,
                "drivewheel":  drivewheel,
                "wheelbase":   wheelbase,
                "boreratio":   boreratio,
                "fuelsystem":  fuelsystem,
                "citympg":     citympg,
                "highwaympg":  highwaympg
            }])

            prediction = round(float(model.predict(sample)[0]), 2)

            return redirect(url_for("result", value=prediction))

        except Exception as e:

            return redirect(url_for("result", value=f"Error: {e}"))

    return render_template("predict.html")


@app.route("/result")
def result():
    value = request.args.get("value", "N/A")
    return render_template("result.html", prediction=value)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
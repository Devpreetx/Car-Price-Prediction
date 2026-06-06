import joblib
import pandas as pd
import os

print(os.getcwd())

# Load model
model = joblib.load("car_price_model.pkl")

print("Enter car details:\n")

enginesize = float(input("Engine Size (50-350): "))
curbweight = float(input("Curb Weight (1500-4500): "))
horsepower = float(input("Horsepower (50-300): "))
carwidth = float(input("Car Width (60-75): "))
carlength = float(input("Car Length (140-210): "))
drivewheel = int(input("Drive Wheel (0/1/2): "))
wheelbase = float(input("Wheelbase (85-120): "))
boreratio = float(input("Bore Ratio (2-4): "))
fuelsystem = int(input("Fuel System (0-7): "))
citympg = int(input("City MPG (10-50): "))
highwaympg = int(input("Highway MPG (15-55): "))

# Create dataframe
sample = pd.DataFrame([{
    "enginesize": enginesize,
    "curbweight": curbweight,
    "horsepower": horsepower,
    "carwidth": carwidth,
    "carlength": carlength,
    "drivewheel": drivewheel,
    "wheelbase": wheelbase,
    "boreratio": boreratio,
    "fuelsystem": fuelsystem,
    "citympg": citympg,
    "highwaympg": highwaympg
}])

# Predict
prediction = model.predict(sample)

print("\nPredicted Car Price:", round(prediction[0], 2))
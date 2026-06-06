import pandas as pd
import kagglehub
path = kagglehub.dataset_download("hellbuoy/car-price-prediction")
print("Path to dataset files:", path)

data = pd.read_csv(path + "/CarPrice_Assignment.csv")
print(data.head(5))
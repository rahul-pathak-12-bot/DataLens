import pandas as pd
from google.colab import files
import os
uploaded = files.upload()
filename = list(uploaded.keys())[0]

data = pd.read_excel(filename, sheet_name="Data")
cost = pd.read_excel(filename, sheet_name="Cost")
shift_running = pd.read_excel(filename, sheet_name="Shift_Running")
actual_output = pd.read_excel(filename, sheet_name="Actual_Output")
scrap = pd.read_excel(filename, sheet_name="Scrap")

# Question 1:Which BS4 only Gear Assembly saw the maximum sales in the first quarter of any given year?
data[(data["GA Category"]=="BS4 Only") & (data["Quarter"]=="Q1")].sort_values(by="Sales Quantity", ascending=False)["Gear Assembly"].values[0]


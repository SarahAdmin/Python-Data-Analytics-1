import pandas as pd 
salesData = pd.read_csv("Sales-2024-10.csv") 
print(salesData.to_string())
salesAverage = salesData["Sales_Volume"].mean() 
print(f'The average sales volume is {salesAverage}') 


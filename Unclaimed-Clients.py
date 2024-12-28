import pandas as pd 
data1 = pd.read_csv('UnclaimedEstatesList.csv') 
print(data1.where(data1["Marital Status"] == 'unknown')

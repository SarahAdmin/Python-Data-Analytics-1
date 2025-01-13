import pandas as pd 

sdf = pd.read_csv('New-and-Old-2024-09.csv')
NewSDF = sdf.drop(columns=['Date','Region_Name','Area_Code']) 
print(NewSDF.corr(method='pearson', min_periods= 1, numeric_only=False))

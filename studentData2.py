import pandas as pd 

df2 = pd.read_csv('data2.xlsx - Bike Sales.csv')

print(df2.to_string()) 
print('Group of Bikes:')
print(df2.groupby())
print(df2.describe())

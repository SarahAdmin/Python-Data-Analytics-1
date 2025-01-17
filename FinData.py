import pandas as pd 

df1 = pd.read_csv('finance_data1.csv',header=0, sep=',')
new_df = df1.dropna(axis=0, inplace=True) 
print(new_df.to_string())

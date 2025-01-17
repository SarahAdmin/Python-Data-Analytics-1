import pandas as pd 

df1 = pd.read_csv('finance_data1.csv')
new_df = df1.dropna() 
print(new_df.to_string())

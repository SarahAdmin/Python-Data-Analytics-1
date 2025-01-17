import pandas as pd 

df1 = pd.read_csv('03 - June.csv', encoding='latin-1')
print(df1.where(df1['Supplier'] == 'IBM UK LTD').dropna(axis=0, inplace=True))

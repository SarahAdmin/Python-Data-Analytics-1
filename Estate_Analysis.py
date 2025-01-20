import pandas as pd 
edf = pd.read_csv('UnclaimedEstatesList_1.csv',encoding='latin-1')
print(edf.where(edf['Marital Status'] == 'spinster')) 

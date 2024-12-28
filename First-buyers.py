import pandas as pd 
hdf = pd.read_csv('First-Time-Buyer-Former-Owner-Occupied-2024-10.csv') 
data1 = hdf.dropna() 
print(data1)

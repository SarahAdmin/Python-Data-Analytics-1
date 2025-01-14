import pandas as pd 
hdf = pd.read_csv('03 - June.csv')
print(hdf.to_string()) 
total_amount = hdf["Amount"].sum() 
average_amount = hdf["Amount"].mean() 
print(f'The Total Amount for NHS is {total_amount}.') 
print(f'The Average Amount for NHS is {average_amount}.')

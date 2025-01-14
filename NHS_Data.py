import pandas as pd 
hdf = pd.read_csv('03 - June.csv', encoding='latin-1')
print(hdf.head(101)) 
hdf['Amount'] = pd.to_numeric(hdf['Amount'].str.replace('[^0-9.-]', '', regex=True))
total_amount = hdf["Amount"].sum() 
average_amount = hdf["Amount"].mean() 
print(f'The Total Amount for NHS is {total_amount}.') 
print(f'The Average Amount for NHS is {average_amount}.')

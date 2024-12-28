import pandas as pd 
hdf = pd.read_csv('New-and-Old-2024-09.csv')   
print(hdf)
total_new_price = hdf['New_Build_Average_Price'].sum() 
print(f"The total price for new building is: {total_new_price}")  
total_e_price = hdf['Existing_Property_Average_Price'].sum() 
print(f"The total price for existing building is {total_e_price}") 


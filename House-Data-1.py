import pandas as pd 
hdf = pd.read_csv('New-and-Old-2024-09.csv') 
data2 = hdf.dropna()  
print(data2.to_string())
average_new_price = data2['New_Build_Average_Price'].mean() 
print(f"The average price for new building is: {average_new_price}")  
average_e_price = data2['Existing_Property_Average_Price'].mean() 
print(f"The average price for existing building is {average_e_price}") 


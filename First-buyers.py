import pandas as pd 
hdf = pd.read_csv('First-Time-Buyer-Former-Owner-Occupied-2024-10.csv') 
total_first_time_price = hdf["First_Time_Buyer_Average_Price"].sum() 
total_former_price = hdf["Former_Owner_Occupier_Average_Price"].sum() 
print(f"The total price of First Time Buyer Price is {total_first_time_price}.")
print(f"The total price of Former Buyer Price is {total_former_price}.")



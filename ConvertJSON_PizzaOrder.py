import pandas as pd 
studentData = {"Name":['Lee Cox','Matt Bond','Joe Malone','Jenny Banks','Marcellina Adams','Paige Quinn','John Baxter'],
              "Topping":['Meat Feast','Pepperoni','Meat Feast','BBQ Chicken','Pepperoni','Cheese and Tomato','Meat Feast'],
              "Size":[10,8,8,10,8,8,10], 
              "Price":[7.50,5.00,5.00,7.50,5.00,5.00,7.50]}
additionalData = {"Allergies":[False,False,False,False,False,False,False]}

var1 = pd.DataFrame(studentData) 
var2 = pd.DataFrame(additionalData) 
odf = var1.join(var2) 
print(odf.to_string())
total_price = odf['Price'].sum()
print(f"The total of the order is {total_price}.")
newODF = odf_to_json()

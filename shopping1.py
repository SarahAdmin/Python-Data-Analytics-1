import pandas as pd 
myData2 = { 
  'Customer_ID':[12,43,64,67,95,29],
  'Customer_Name':['Lee Cox','Matt Bond','Marcy Rogers','Lana Montana','Amy Adams','Marie Quinn'],
  'Product':['Desk','Desk','Chair','Shelf','Bookshelf','Lamp'],
  'Order_ID':[1,2,3,4,5,6]
}
myVariables = pd.DataFrame(myData2) 
print(myVariables)

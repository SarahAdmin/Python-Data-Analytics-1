import pandas as pd 
myData2 = { 
  'Customer_ID':[12,43,64,67,95,29],
  'Customer_Name':['Lee Cox','Matt Bond','Marcy Rogers','Lana Montana','Amy Adams','Marie Quinn'],
  'Product':['Desk','Desk','Chair','Shelf','Bookshelf','Lamp'],
  'Order_ID':[1,2,3,4,5,6]
}
shop1 = { 
      'Price':[120.00,120.00,10.00,65.84,200.50,30.59], 
      'Delivery':[False,True,False,True,True,True]
}
myVariables = pd.DataFrame(myData2) 
MyVar2 = pd.DataFrame(shop1) 
DataFour = myVariables.join(MyVar2)
print(DataFour)
totalPrice = DataFour.groupby("Customer_ID")["Price"].sum() 
print(f"The total price altogether is {totalPrice}")

DataFour.to_csv('MyShopping.csv',index=False)

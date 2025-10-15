import pandas as pd
def PizzaParty(input_data,columns_names): 
    df1 = pd.DataFrame(input_data,columns=columns_names)
    return df1 

data =[['Lee Cox','Pepperoni','Medium'],['Lemon Jelly','Meat Feast','Medium'],['Gill Gates','BBQ Chicken','Small'],['Matt Bond','Hawaiian','Small']]
cols = ['Name','Toppings','Size']
final_data = PizzaParty(data,cols)
print(final_data)

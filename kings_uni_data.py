import pandas as pd
def Kings_Students(input_data,columns_names):
  df = pd.DataFrame(input_data,columns=columns_names)
  return df 

data = [[1,'Lee Cox','Computer Science'],
        [2,'Lemon Jelly','Finance'],
        [3,'Gill Gates','Computer Science'], 
        [4,'Matt Bond','Media']]
cols = ['ID','Name','Course'] 
inventory_data = Kings_Students(data,cols)
print(inventory_data)

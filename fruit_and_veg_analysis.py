import pandas as pd 
fvdf = pd.read_csv('fruitvegprices-250107.csv', encoding='latin-1')
print(fvdf.describe())

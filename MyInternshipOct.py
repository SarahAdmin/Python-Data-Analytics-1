import pandas as pd 
OctDF = pd.read_csv('October Feedback.csv') 
newOct = OctDF.dropna() 
print(newOct)

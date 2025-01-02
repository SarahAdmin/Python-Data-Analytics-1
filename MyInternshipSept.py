import pandas as pd 
SeptDF = pd.read_csv('September Feedback.csv') 
NewSeptD = SeptDF.dropna() 
print(NewSeptD)

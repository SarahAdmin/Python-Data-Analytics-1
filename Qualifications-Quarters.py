import pandas as pd 

data1 = pd.read_csv('regulated-qualifications-dataset-Jan-2012-to-present-England.csv')
qdf1 = data1.dropna() 
print(qdf1) 

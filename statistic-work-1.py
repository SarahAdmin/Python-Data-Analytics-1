import pandas as pd 
df = pd.read_csv('HMCTS_MI_output_accessible (2).csv',encoding='latin-1') 
finalDF = df.style.background_gradient(cmap='BuGr')
print(finalDF.to_string())

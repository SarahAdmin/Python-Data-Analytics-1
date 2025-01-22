import pandas as pd 
jobData = pd.read_csv('permanent-and-temporary-employment-2021.csv',encoding='latin-1')
print('Permanent Jobs in 2021')
print(jobData.head(101).where(jobData["employment_type"] == 'Permanent'))

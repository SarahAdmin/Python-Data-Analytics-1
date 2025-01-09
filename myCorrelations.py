import pandas as pd 

latedf = pd.read_csv('CSV_HMCTS_management_information_Nov23toNov24.csv')
print(latedf.corr())

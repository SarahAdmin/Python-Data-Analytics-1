import sys  
import matplotlib 
matplotlib.use('Agg')

import pandas as pd 
import matplotlib,pyplot as plt 

latedf = pd.read_csv('CSV_HMCTS_management_information_Nov23toNov24.csv')
newlatedf = latedf.drop(columns=["Month"])

newlatedf.plot() 

plt.show()


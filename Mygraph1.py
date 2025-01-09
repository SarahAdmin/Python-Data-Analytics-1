import sys  
import matplotlib 
matplotlib.use('Agg')

import pandas as pd 
import matplotlib,pyplot as plt 

latedf = pd.read_csv('CSV_HMCTS_management_information_Nov23toNov24.csv')

latedf.plot() 

plt.show()

plt.savefig(sys.stdout.buffer) 
sys.stdout.flush()

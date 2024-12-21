import pandas as pd 

data1 = { 'Number_of_bits': [8,16,8,24,128,256,255], 
         'Memory':[128,256,255,256,4096,32,64]
        }
df1 = pd.DataFrame(data1) 

print(df1.pow(2))

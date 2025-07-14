import pandas as pd 
driveDF = pd.read_csv('drt121e-car-driving-tests-with-zero-faults.csv',encoding='latin-1') 
finalDF = driveDF.style.background_gradient(cmap='Oranges')
print(finalDF.to_string())

import pandas as pd 
driveDF = pd.read_csv('drt121e-car-driving-tests-with-zero-faults.csv')
print(driveDF.describe())

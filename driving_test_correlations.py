import pandas as pd 

drivedf = pd.read_csv('drt121e-car-driving-tests-with-zero-faults.csv')
drivedf.drop(columns['Year','Car driving test pass rate','Percentage of car driving test conducted with zero faults','Percentage of car driving test passes with zero faults'])
print(drivedf.corr(method='pearson', min_periods= 1, numeric_only=False))

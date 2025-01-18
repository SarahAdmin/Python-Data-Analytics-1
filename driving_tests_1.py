import pandas as pd 
driveDF = pd.read_csv('drt121e-car-driving-tests-with-zero-faults.csv')
# Print the column names to verify the correct names
print(driveDF.columns)  
# Modify the code to access the columns using their correct names from the output above
for column in driveDF.columns[1:4]:
    driveDF[column] = pd.to_numeric(driveDF[column].str.replace('[^0-9.-]', '', regex=True), errors='coerce')
average_score_1 = driveDF[driveDF.columns[1]].mean()
average_score_2 = driveDF[driveDF.columns[2]].mean()
average_score_3 = driveDF[driveDF.columns[3]].mean()
print(f"The Average of Total Car Driving Tests Conducted is {average_score_1}.")
print(f"The Average of Total Car Driving Tests Passed is {average_score_2}.")
print(f"The Average of Total Car Driving Tests Passed with Zero Faults is {average_score_3}.")

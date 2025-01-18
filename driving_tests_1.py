import pandas as pd 
driveDF = pd.read_csv('drt121e-car-driving-tests-with-zero-faults.csv')
print(driveDF.to_string()); 
for column in ["Total car driving tests conducted","Total car driving tests passed","Total car driving tests passed with zero faults"]:
    driveDF[column] = pd.to_numeric(driveDF[column].str.replace('[^0-9.-]', '', regex=True), errors='coerce')
average_score_1 = driveDF["Total car driving tests conducted"].mean() 
average_score_2 = driveDF["Total car driving tests passed"].mean()
average_score_3 = driveDF["Total car driving tests passed with zero faults"].mean()
print(f"The Average of Total Car Driving Tests Conducted is {average_score_1}.")
print(f"The Average of Total Car Driving Tests Passed is {average_score_2}.")
print(f"The Average of Total Car Driving Tests Passed with Zero Faults is {average_score_3}.")

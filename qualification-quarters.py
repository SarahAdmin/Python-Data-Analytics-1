import pandas as pd 
df1 = pd.read_csv('regulated-qualifications-dataset-Jan-2012-to-present-England.csv', encoding='latin-1')
print(df1.head(51)) 

average_quarter_1_2023 = df1[2023.1].mean() 
average_quarter_2_2023 = df1[2023.2].mean() 
average_quarter_3_2023 = df1[2023.3].mean() 
average_quarter_4_2023 = df1[2023.4].mean() 
average_quarter_1_2024 = df1[2024.1].mean() 
average_quarter_2_2024 = df1[2024.2].mean() 
average_quarter_3_2024 = df1[2024.3].mean() 

print(f"The average result of first quarter of 2023 is {average_quarter_1_2023}.")
print(f"The average result of second quarter of 2023 is {average_quarter_2_2023}.")
print(f"The average result of third quarter of 2023 is {average_quarter_3_2023}.")
print(f"The average result of fourth quarter of 2023 is {average_quarter_4_2023}.")
print(f"The average result of first quarter of 2024 is {average_quarter_1_2024}.")
print(f"The average result of second quarter of 2024 is {average_quarter_2_2024}.")
print(f"The average result of third quarter of 2024 is {average_quarter_3_2024}.")




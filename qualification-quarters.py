import pandas as pd 
df1 = pd.read_csv('regulated-qualifications-dataset-Jan-2012-to-present-England.csv', encoding='latin-1')
print(df1.head(51)) 
for column in ["2023.1", "2023.2", "2023.3", "2023.4", "2024.1", "2024.2", "2024.3"]:
    df1[column] = pd.to_numeric(df1[column].str.replace('[^0-9.-]', '', regex=True), errors='coerce')

average_quarter_1_2023 = df1["2023.1"].mean() 
average_quarter_2_2023 = df1["2023.2"].mean() 
average_quarter_3_2023 = df1["2023.3"].mean() 
average_quarter_4_2023 = df1["2023.4"].mean() 
average_quarter_1_2024 = df1["2024.1"].mean() 
average_quarter_2_2024 = df1["2024.2"].mean() 
average_quarter_3_2024 = df1["2024.3"].mean() 

print(f"The average result of first quarter of 2023 is {average_quarter_1_2023}.")
print(f"The average result of second quarter of 2023 is {average_quarter_2_2023}.")
print(f"The average result of third quarter of 2023 is {average_quarter_3_2023}.")
print(f"The average result of fourth quarter of 2023 is {average_quarter_4_2023}.")
print(f"The average result of first quarter of 2024 is {average_quarter_1_2024}.")
print(f"The average result of second quarter of 2024 is {average_quarter_2_2024}.")
print(f"The average result of third quarter of 2024 is {average_quarter_3_2024}.")



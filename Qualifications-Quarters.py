import pandas as pd 

data1 = pd.read_csv('regulated-qualifications-dataset-Jan-2012-to-present-England.csv')
quarter2023One = data1["2023.1"].mean() 
quarter2023Two = data1["2023.2"].mean() 
quarter2023Three = data1["2023.3"].mean() 
quarter2023Four = data1["2023.4"].mean() 
quarter2024One = data1["2024.1"].mean() 
quarter2024Two = data1["2024.2"].mean() 
quarter2024Three = data1["2024.3"].mean() 

print(f"The Average first quarter of 2023 is {quarter2023One}") 
print(f"The Average second quarter of 2023 is {quarter2023Two}") 
print(f"The Average third quarter of 2023 is {quarter2023Three}") 
print(f"The Average fourth quarter of 2023 is {quarter2023Four}") 
print(f"The Average first quarter of 2024 is {quarter2024One}") 
print(f"The Average second quarter of 2024 is {quarter2024Two}") 
print(f"The Average third quarter of 2024 is {quarter2024Three}") 


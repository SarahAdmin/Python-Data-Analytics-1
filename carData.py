import pandas as pd 

myData2 = { 
'Make': ["Toyota","Ford","Volkswagen"],
'Model':["Yaris,","Fiesta","T-Cross"], 
'Colour':["Red","Blue","Black"], 
'No_of_Seats':[5,5,5], 
'Year':[2019,2024,2020]
}
myD1 { 
"Type of Petrol": ["Unleaded","Unleaded","Unleaded"]
}
myVar1 = pd.DataFrame(myData2) 
myVar2 = pd.DataFrame(myD1) 
myCars = myVar1.join(myVar2)
print(myCars)

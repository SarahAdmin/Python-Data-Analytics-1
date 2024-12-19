import pandas as pd 

myData = { 
'student_id': [285,100,495],
'name': ["Lee Cox","Matt Bond","Lemon Jelly"],
'course':["Computing","Finance","Accounting"]

}
myVar = pd.DataFrame(myData) 
print(myVar)

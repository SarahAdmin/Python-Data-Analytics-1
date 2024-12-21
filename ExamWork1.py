import pandas as pd 

StudentData1 = {"Name":['Lee Cox','Matt Bond','Lemon Jelly','Marcellina Adams','Jill Gates','Joe Malone'], 
                "Qualification":['FS','FS','FS','FS','FS','FS'],
                "Level":['L1','L1','E3','E3','L1','E3'],
                "Subject":['English','English','English','English','English','English']
                "Passed":[True,True,True,False,False,True]
              }

Variables2 = pd.DataFrame(StudentData1) 
print(Variables2)

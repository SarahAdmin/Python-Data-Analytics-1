import pandas as pd 

StudentData1 = {"Name":['Lee Cox','Matt Bond','Lemon Jelly','Marcellina Adams','Jill Gates','Joe Malone'], 
                "Qualification":['FS','FS','FS','FS','FS','FS'],
                "Level":['L1','L1','E3','E3','L1','E3'],
                "Subject":['English','Maths','English','Maths','English','Maths'],
                "Passed":[True,True,True,False,False,True]
              }
StudentData2 = { "Retake?": [False,False,False,True,True]
             } 

Variables2 = pd.DataFrame(StudentData1) 
df3 = pd.DataFrame(StudentData2) 
Results  = Variables2.join(df3)
print(Results)

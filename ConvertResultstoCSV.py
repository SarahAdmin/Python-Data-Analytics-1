import pandas as pd 

StudentData1 = {"Name":['Lee Cox','Matt Bond','Lemon Jelly','Marcellina Adams','Jill Gates','Joe Malone'], 
                "Qualification":['FS','FS','FS','FS','FS','FS'],
                "Level":['L1','L1','E3','E3','L1','E3'],
                "Subject":['English','Maths','English','Maths','English','Maths'],
                "Pecentage":[70,100,65,30,40,80],
                "Passed":[True,True,True,False,False,True]
              }
StudentData2 = { "Retake?": [False,False,False,True,True,False]
             } 


Variables2 = pd.DataFrame(StudentData1) 
Variables2.insert(1,"Course", ["L1 Media","L1 ICT","L1 Beauty","L1 ICT","L1 ICT","L1 Media"])
df3 = pd.DataFrame(StudentData2) 
Results  = Variables2.join(df3)
print(Results)

FinalResults = Results.to_csv('Student_Results.csv',index=False)

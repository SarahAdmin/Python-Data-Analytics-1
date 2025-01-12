import numpy as np 
myArr1 = np.array(['Milkshake','Cola','Tea','Coffee','Diet Cola','Orange Juice','Apple Juice']) 
myArr2 = np.array(['Fries','Cheeseburger','Hamburger','Hot Dog','Pizza',])

myArr = np.concatenate((myArr1,myArr2))

print(myArr)

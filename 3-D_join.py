import numpy as np

myArr1 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
myArr2 = np.array([[[10,11,12],[13,14,15],[15,17,18]]]) 
myArray = np.concatenate((myArr1,myArr2)) 
print(myArray)

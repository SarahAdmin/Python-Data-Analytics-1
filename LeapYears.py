import numpy as np 

myYears1 = np.array([1980,1981,1982,1983,1984,1985,1986,1987,1988,1989])
myYears2 = np.array([1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009])
myLeapYears = np.concatenate((myYears1,myYears2)) 

finalOne = np.where((myLeapYears%4 == 0))

print(finalOne)

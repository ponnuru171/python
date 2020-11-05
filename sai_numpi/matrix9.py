import numpy as np
x=np.array([[1,2,3,4,5,6,7,8],[9,8,7,6,5,4,3,2]])
print(x)
print("specific row")
print(x[0,:])
print("specific coloumn")
print(x[:,1])
print(x[0,1:6:2])
x[1,5]=100
print(x)
x[:,2]=[60,70]
print(x)
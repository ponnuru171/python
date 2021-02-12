import numpy as np
x=np.array([input("enter 1st row").split(),input("enter 2nd row").split()])
print(x)
print(np.linalg.det(x))
import numpy as np
x=np.array([[1,2],[6,7]])
print(type(x))
y=np.array([[6,7],[1,2]])
print(type(y))
z=x + y
a=x - y
print(z)
print(type(z))
print("-----------------------------------------------------------")
print(a)
print("-----------------------------------------------------------")
b=z * a
print(b)
print("-----------------------------------------------------------")
c=2 * b
print(c)


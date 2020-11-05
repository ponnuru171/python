p=1
l=[1,2,3,4,5,6]
for i in l:
    p *= i
print(p)
from functools import reduce
def prod(x,y):
    return x * y
prod1=reduce(prod,l)
print(prod1)

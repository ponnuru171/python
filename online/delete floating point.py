a=int(input("enter the number of values "))
b=[]
for i in range(a):
    c=input("enter the values ")
    print(type(c))
    b.append(c)
print(b)
for j in range(len(b)):
    cf=isinstance(b[j],float)
    print(b[j]," is ",cf)
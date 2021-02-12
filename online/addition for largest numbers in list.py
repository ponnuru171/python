a=int(input("enter the number of list"))
g=int(input("enter number for divisible"))
e=[]
for j in range(0,a):
    d=int(input("enter the size of list"))
    b=[]
    for i in range(0,d):
        c=int(input("enter elements"))
        b.append(c)
        b.sort()
    print(b)
    e.append(b[-1])
f=[]
for k in range(len(e)):
    h= int(e[k]) * int(e[k])
    f.append(h)
print(sum(f) % g)


#another method
"""a=int(input("enter the size of list"))
d=[]
g=int(input("enter the number for percentile"))
for i in range(0,a):
    b=input("enter the elements")
    c=list(b)
    print(c)
    c.sort()
    print(c)
    d.append(c[-1])
print(d)
f=[]
for j in range(0,len(d)):
    e= int(d[j]) * int(d[j])
    f.append(e)
print(sum(f) % g)
"""
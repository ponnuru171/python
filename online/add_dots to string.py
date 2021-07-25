a=list(input("enter the data "))
b=[]
c=''
for i in range(0,len(a)):
    if(len(a) == i+1):
        b.append(a[i])
    else:
        b.append(a[i])
        b.append('.')
print(c.join(b))
"""d=list(c)
e=""
for i in range(0,len(c)):
    if (c[i]=="."):
        d.pop()
    else:
        continue
print(e.join(d))"""
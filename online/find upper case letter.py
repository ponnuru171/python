a=list(input())
c=[]
for b in range(0,len(a)):
    if(a[b].isupper() == True):
        c.append(a[b])
print(c)
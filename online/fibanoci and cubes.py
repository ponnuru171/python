x=int(input())
f=0
c=1
s=[]
for i in range(0,x):
    f1=f+c
    c=f
    f=f1
    s.append(f1)
print(s)
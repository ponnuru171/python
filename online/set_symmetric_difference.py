a=int(input())
b=[]
for i in range(0,a):
    c=int(input())
    b.append(c)
g=set(b)
print(g)
d=int(input())
e=[]
for j in range(0,d):
    f=int(input())
    e.append(f)
h=set(e)
print(h)
i=g.symmetric_difference(h)
print(len(i))
#another method
"""N1 = int(input())
a = set(input().split())
print(a)
N2 = int(input())
b = set(input().split())
print(b)
storage3 = a.symmetric_difference(b)
print(len(storage3))
"""
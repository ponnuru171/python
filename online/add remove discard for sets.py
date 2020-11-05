a=int(input("enter the number of elements  "))
c=[]
for i in range(0,a):
    b=input()
    c.append(b)
print(c)
d=int(input("enter the no.of commands to execute "))
print(d)
h=set(c)
for j in range(0,d):
    e=str(input())
    if e == 'pop':
        h.pop()
    elif e == 'discard':
        g=input("enter the element to discard ")
        h.discard(g)
    elif e == 'remove':
        f=input("enter element to remove ")
        h.remove(f)
    else:
        continue
print(list(h))
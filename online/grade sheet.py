a=int(input("enter the row "))
b=int(input("enter the coloumn "))
e=[]
for i in range(a):
    c=[]
    for j in range(b):
        d=int(input())
        c.append(d)
    avg= sum(c) / b
    e.append(avg)
    print(c)
print(e)
f=[]
for ij in range(len(e)):
    if e[ij] >= 90:
        f.append("A+")
    elif e[ij] >= 80:
        f.append("A")
    elif e[ij] >= 70:
        f.append("B")
    elif e[ij] >= 60:
        f.append("C")
    elif e[ij] >= 50:
        f.append("D")
    else:
        f.append("F")
print(f)
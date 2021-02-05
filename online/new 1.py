a=[]
for i in range(0,2):
    b=int(input("enter the number"))
    a.append(b)
print(a)
x=1
for j in range(0,1000):
    if a[j] % x == 0:
        print(j)
        x = x + 1
    else:
        continue

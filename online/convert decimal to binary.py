a=int(input("enter the number"))
b=[]
for i in range(a):
    if a==1:
        b.append(a)
        break
    else:
        c=a%2
        b.append(c)
        a=round(a//2)
        print(a)
print(b[::-1])
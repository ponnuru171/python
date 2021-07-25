a=input("enter data ")
b=len(a)
if b % 2 == 0:
    c=b/2
    d=int(c)
    print(a[d])
else:
    c=b//2
    print(c)
    print(a[c])
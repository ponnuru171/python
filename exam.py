def a(list,b):
    c=0
    for i in range(b):
        d=list(i)
        if d%2 == 0:
            continue
        else:
            c=list(i)+c
            return c
A=a([1,3,5,15,22],5)
print(A)
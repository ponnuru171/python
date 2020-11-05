x=int(input("enter the number "))
for i in range(0,x + 1):
    a=bin(i)
    b=oct(i)
    c=hex(i)
    print(i,"   ",b[2:],"   ",c.upper()[2:],"   ",a[2:])

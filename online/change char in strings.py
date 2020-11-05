x=input("enter the string  ")
a=int(input("enter the position to change  "))
b=input("enter the char to paste   ")
y=list(x)
y[a]=b
c="".join(y)
print(c)
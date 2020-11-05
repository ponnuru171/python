x=range(1,40)
print(list(x))
def divide(num):
    if (num % 5) == 0:
        return num
p = list(filter(divide, x))
print("divisibles of 5 upto are" ,p)


from functools import reduce
def square(num1):
    return(num1**2)
s=list(map(square,p))
print("square for divisibles of 5 upto 40 are ",s)


def fa(y,z):
    return y * z
fact=reduce(fa,p)
print("factorial for divisibles of 5 upto 40 is ",fact)


print(s)
for i,j in enumerate(s):
    print(i,j)

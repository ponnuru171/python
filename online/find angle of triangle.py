import math as m
x=int(input("""enter which angle u want
1 for sin
2 for cos
3 for tan  
"""))
if x == 1:
    a=int(input("enter the opposite side of triangle "))
    b=int(input("enter the hypotenuse side of triangle "))
    c = a / b
    d=m.asin(c)
    e=m.degrees(d)
    print("The angle is ",e," degrees")
if x == 2:
    a1 = int(input("enter the adjacent side of triangle "))
    b1 = int(input("enter the hypotenuse side of triangle "))
    c1 = a1 / b1
    d1 = m.asin(c1)
    e1 = m.degrees(d1)
    print("The angle is ", e1," degrees")
if x == 3:
    a2 = int(input("enter the opposite side of triangle "))
    b2 = int(input("enter the adjacent side of triangle "))
    c2 = a2 / b2
    d2 = m.asin(c2)
    e2 = m.degrees(d2)
    print("The angle is ", e2, " degrees")
else:
    exit()
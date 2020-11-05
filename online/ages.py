n=int(input("enter no of ages  "))
for i in range(0,n):
    x = int(input("enter the age   "))
    if 0 < x < 10:
        print("you are child")
        print("you are child")
    elif 10 < x < 19:
        print("you are teenager")
        print("you are tennager")
    elif 19 < x < 30:
        print("you are young")
        print("you are young")
    elif x > 29:
        print("you are old")
    else:
        print("age is not valid enter correct age")
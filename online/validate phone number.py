a=int(input("enter number of phone numbers "))
for i in range(a):
    b= input("enter the 10 digits number ")
    c=list(b)
    print(len(c))
    print(c[0])
    if (len(c) == 10 ):
        if (c[0] == 9 or c[0] == 8 or c[0] == 7):
            print("valid number")
        else:
            print("unknown")
    else:
        print("invalid number")
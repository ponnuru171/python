a=int(input("enter number of phone numbers "))
j=0
for i in range(a):
    b= input("enter the 10 digits number ")
    c=list(b)
    if (len(c) == 10 ):
        if (c[j] == 9 or c[j] == 8 or c[j] == 7):
            print("valid number")
        else:
            print("unknown")
    else:
        print("invalid number")
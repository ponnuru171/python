x=int(input("enter loin id"))
y=int(input("enter password"))
if x == 123456:
    print("continue")
    if y == 98765:
        print("login sucessfull")
    else:
        print("enter password correctly")
else:
    print("enter loin id correctly")
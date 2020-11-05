x=int(input("enter the x value"))
if x > 1:
    for i in range(2,x):
        if(x % i) == 0:
            print("checking")
            break
    else:
        print(x,"is prime number")
else:
    print("it is not prime number")

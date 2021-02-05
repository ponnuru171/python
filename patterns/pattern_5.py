a=int(input("enter the number "))
for b in range(1,a+1):
    for c in range(1,a+1):
        if b + c == a + 1:
            print(b,end="")
        else:
            print(" ",end="")
    print()
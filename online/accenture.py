a=int(input("enter the number  "))
for i in range(0, a):
    if a % 2 == 0:
        a = a / 2
    else:
        a = a - 1
    if a == 0:
        print(i + 1)
        exit()
    else:
        continue
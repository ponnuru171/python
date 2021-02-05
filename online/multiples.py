a=int(input("enter the multiple number "))
b=int(input("enter the no of tables "))
count = 0
for c in range(0,1000):
    if c % a == 0:
        count = count + 1
        print(c)
        if count == b:
            break
        else:
            continue
    else:
        continue
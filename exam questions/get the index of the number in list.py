a=list(input("enter the jesery number of students "))
b=int(input("enter the jersey number to get the position "))
a = [int(i) for i in a]
a.sort()
print(a)
for i in range(len(a)):
    if b == a[i]:
        print(i)
        continue
    else:
        a.sort()
        print(a.index(b))
        break

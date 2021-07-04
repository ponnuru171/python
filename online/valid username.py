a=input("enter user name ")
b=["sai","siva","vishnu","lucky"]
c=0
for i in range(0,len(b)):
    if b[c] == a:
        print( a, "already exist please enter new ")
        c = c + 1
        break
    else:
        b.append(a)
        print("creating ",a," sucessfull")
        break

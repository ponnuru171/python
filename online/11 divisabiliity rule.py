a=input("enter the number  ")
b=list(a)
c=int(a)
d=len(b)
eve=0
odd=0
for i in range(1,d+1):
    if d % 2 == 0:
        eve = eve + c%10
    else:
        odd = odd + c%10
    c = c // 10
    d = d - 1
print(eve-odd)
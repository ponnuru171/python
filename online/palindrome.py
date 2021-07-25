x=int(input("enter the x value"))
rev=0
temp=x
while x > 0:
    rem = x % 10
    rev = (rev * 10) + rem
    x = x // 10
    print(x)
if(temp == rev):
    print("it is palindrome")
else:
    print("it is not palindrome")
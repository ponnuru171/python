x=int(input("enter the x value "))
y=int(input("enter the y value "))
for num in range(x,y):
    if num > 1:
         for i in range(2,num):
             if(num % i) == 0:
                 break
         else:
             print(num)
print(num)

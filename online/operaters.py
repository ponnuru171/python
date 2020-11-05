mc=float(input("enter the meal cost  "))
y=int(input("enter the tip percent  "))
z=int(input("enter the tax "))
tip=mc*(y/100)
tax=mc*(z/100)
total=mc+tax+tip
print(round(total))

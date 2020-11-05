x=[1,2,5,3,4,3,2,1,"a","b"]
y=set(x)
c=list(y)
print(c)
c.remove(4)
print(c)
c.pop()
print(c)
cp_x=x.copy()                    # command is used for copy
print(cp_x)
print(x + cp_x)                  # command is used for concerent
print((x + cp_x).count(1))
print(2 in x + cp_x)
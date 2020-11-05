x=(1,2,3,4,5,6,7,8,9,1,1,1,1,1)
print(x.count(1))
print(9 in x)                         # command is used to check the element in tuple
y=[12,13,14,15,16]
a=tuple(y)
print(type(a))
#b=(tuple(input()))
#print(b)
print(x[2:6])                         # command is used to slicing the tuple
x=x[:-1] + (15,12,13)                 # command is used to add the elements to tuple
print(x)
index=x.index(15)
print(index)
x1=5,                                  # command is used to create an item using tuple
print(x1)
g=(1,2,3,4,5,6)
h=str(g)
print(h)
i=("ponnuru")
print(reversed(i))
e=((5171,"ponnuru"),(5162,"srinu"),(5142,"ghani"),(5009,"chandu"))
print(dict((y,x) for x,y in e))         # command is used to convert tuple to dictonary

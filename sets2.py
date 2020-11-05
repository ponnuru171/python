x={1,2,3,4,5}
y={3,4,5,6,7}
print(x | y)                         # This statement print total values in x and y
print(x & y)                         # This statement print common values in x and y
print(x.union(y))                    # This statement print total values in x and y
print(x.intersection(y))             # This statement print common values in x and y
print(x.difference(y))               # This statement print difference of x and y
print(x - y)                         # This statement print difference of x and y
a=frozenset([1,2,3,4,5,6])           # # This statement conver the normal set to frozenset.in frozen set we cannot add (or) delete
a.add(5)                             # This statement add value to a
print(a)
a.pop()                              # This statement delete the value in a
print(a)
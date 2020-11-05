x={1,2,3,4,5}
y={3,4,5,6,7}
print(x)
print(type(x))           # This statement print it belongs to which type
#print(x[1])
x.add(0)                 # This statement add single value to set
print(x)
x.update([10,9])         # This statement add multiple values to set
print(x)
x.discard(10)            # This statement delete value in x
print(x)
x.discard(20)            # This statement delete value in x
print(x)
x.remove(9)              # This statement delete value in x
print(x)
x.remove(5)              # This statement delete value in x
print(x)
#Difference between discard and remove. in discard we can delete the number which is not present in the set in remove we cannot do that
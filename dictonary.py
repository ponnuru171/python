x={1:'abc',2:'xyz'}        # This statement of x
print(type(x))             # This statement print y belongs to which type
print(x)
y={'name':'ponnuru','dob':'05/01/1999'}  # This statement of y
print(y)
print(y['name'])           # This statement print the value in name
print(y['dob'])            # This statement print the value in dob
print(y.get('name'))       # This statement print value in name
print(y.get('dob'))        # This statement print value in dob
print(x.get(1))
y['name']='venkat'         # This statement changes the value in name
print(y)
y['city']='nellore'        # This statement add the item to the y
print(y)
print(y.pop('city'))       # This statement delete the item to the y
print(y)
y.popitem()                # This statement delete the last item in y
print(y)
print(x.items())           # This statement print keys and values in x
print(x.keys())            # This statement print the keys in x
print(x.values())          # This statement print the values in x
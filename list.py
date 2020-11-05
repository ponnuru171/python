x=[10,20,30,40,50,60,70]
print(x)
print(type(x))                      # This statement print x belongs to which type
print(x[0])                         # This statement print index 0 value in x
print(x[1])                         # This statement print index 1 value in x
print(x[4])                         # This statement print index 4 value in x
print(x[-1])                        # This statement print last value in x
print(x[-2])
print(x[0:3])                       # This statement print values of x from index 0 to 2
print(x[-1:-3])                     # This statement print empty set because it need to be arranged from low to high
print(x[-3:-1])                     # This statement print values of x from index -3 to -1
print(x[0:])                        # This statement print values of x from index 0 to last
print(x[:2])                        # This statement print values of x from index 0 to 2
print(x[1::3])                      # This statement print value of x from index 1 with gap of 3 elements from 1
x[2]=100                            # This statement replace the value of x in index 2
print(x)
x.append(200)                       # This statement add the value to list on last
print(x)
print(x.index(20))                  # This statement print index of 20 in x
print(x)
x.append(20)                        # This statement add the value to list on last
x.append(10)                        # This statement add the value to list on last
print(x)
print(x.count(20))                  # This statement count the repetation in x
x.pop()                             # This statement delete the value to list on last
print(x)
x.pop()                             # This statement delete the value in list on last
print(x)
x.pop(2)                            # This statement delete the value in list of index 2
print(x)
x.remove(200)                       # This statement delete the particular number in x
print(x)
x.append(10)                        # This statement add the value to list on last
x.append(20)                        # This statement add the value to list on last
print(x)
x.remove(10)                        # This statement delete the particular number in x
print(x)
print(x[0:])                        # This statement print values of x from index 0 to last
print(x[:3])                        # This statement print values of x from index 0 to 3
print(x[3:])                        # This statement print values of x from index 3 to last
print(x[:2])                        # This statement print values of x from index 0 to 2
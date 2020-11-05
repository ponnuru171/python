x={'c':10,'a':20,'b':30}
for dict_key,dict_value in x.items():
    print(dict_key,'-->',dict_value)
a={'ponnuru':5171}
b={'srinu':5162}
c={'ganesh':5142}
d={'chandu':5009}
e={}
for e in (a,b,c,d):
    e.update(e)
    print(e)
print(sum(x.values()))
x_max=max(x.keys(),key=(lambda k:x[k]))                           # command to print the maximum values
print(x_max)
x_min=min(x.keys(),key=(lambda k:x[k]))                           # command to print the minimum values
print(x_min)
f=a.copy()
f.update(b)                           # command is used to concortenate the dictonary
print(f)
for key in sorted(x):                           # command to print the key in order
    print('%s:%s'%(key,x[key]))

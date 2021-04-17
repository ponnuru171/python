a=input()
b=list(a)
print(b)
c=0
for i in range(0,len(b)):
    if(b[i] == 'a' or b[i] == 'e' or b[i] == 'i' or b[i] == 'o' or b[i] == 'u'):
        c = c+1
    else:
        continue
print(c)
a=list(input("enter data "))
b=input("enter the replace char in vowle ")
d=""
for i in range(0,len(a)):
    if (a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
        a.pop(i)
        a.insert(i,b)
    else:
        continue
    i=i+1
print(d.join(a))
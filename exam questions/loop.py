#J3I3N3K2I3E3S2
a="JJJIIINNNKKIIIEEESS"
"""for i in range(len(a)):
    count=1
    for j in range(i+1,len(a)):
        if (a[i] == a[j] and a[i] != ' '):
            count=count+1
            a=a[:j] + '0' + a[j+1:]
    if count > 1 and a[i] !='0':
        print(a[i],count)"""
b=len(a)
for i in range(len(a)):
    count=1
    if len(a) == b:
        break
    else:
        if (a[i] == a[i+1] and a[i] != ' '):
            count = count + 1
            a = a[:i] + '0' + a[(i+1) + 1:]
    if count > 1 and a[i] != 0:
        print(a[i], count)

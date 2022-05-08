a='venkatasai'
for i in range(0,len(a)):
    c=1
    for j in range(i+1,len(a)):
        if (a[i] == a[j] and a[i]!=''):
            c=c+1
            a=a[:j]+'0'+a[j+1]
        if c>1 and a[i]!='0':
            print(a[i])
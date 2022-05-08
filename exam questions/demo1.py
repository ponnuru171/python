"""a=[1,10,4,9,2,6,5]
tmp=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a)"""
a=[1,0,0,1,1,0]
b=[]
print(len(a))
for i in range(len(a)):
    if a[i] == 0:
        b.append(a[i])
    else:
        a.pop(a[i])
    print(a[i])
print(a)
print(b)

"""employee table has id name depid
department table has id dname salary
beeline biwasehouse.department(where(salary >5000)) ;"""
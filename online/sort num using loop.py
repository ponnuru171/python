a=[1,2,3,4,5,65,22,11,9]
tmp=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
print("largest number is ",a[-1])
print("smallest number is ",a[0])
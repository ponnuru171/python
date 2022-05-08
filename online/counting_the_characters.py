#input  abaaabccc
#output aba3bc3
a="abaabbccc"
b=[]
for i in range(len(a)):
    for j in range(1,len(a)):
        c=1
        if (j>i) & (j-i == 1):
            if a[i] == a[j]:
                c = c + 1
                b.append(a[i])
                b.append(c)
            else:
                b.append(a[i])
print(b)
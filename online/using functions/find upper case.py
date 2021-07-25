def capital_indexes(a):
    b=[]
    for i in range(0,len(a)):
        if a[i].isupper():
            b.append(i)
        else:
            continue
    print(b)
    return b
capital_indexes(input())

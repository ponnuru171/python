def vtoc(x,b):
    a=list(x)
    d = ""
    for i in range(0, len(a)):
        if (a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u'):
            a.pop(i)
            a.insert(i, b)
        else:
            continue
        i = i + 1
    print(d.join(a))
    return d
vtoc(input(),input())
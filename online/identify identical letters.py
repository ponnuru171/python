a="sai"
b=sorted(a)
for i in range(0,len(a)+2):
    if (b[i]==b[i+1]):
        print(True)
        break
    else:
        print(False)
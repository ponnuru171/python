a=list(input())
b=0
for i in range(len(a)):
    c=a.pop()
    if c == '1':
        b = b + 2**i
print(b)
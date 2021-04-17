a=set(input().split())
b=set(input().split())
c=a.union(b)
d=a.intersection(b)
e=c-d
for i in sorted(list(e)):
    print(i)
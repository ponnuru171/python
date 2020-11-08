a=set(input().split())
b=int(input())
output=True
for i in range(0,b):
    c=set(input().split())
    if not c.issubset(a):
        output = False
    if len(c) >= len(a):
        output = False
print(output)
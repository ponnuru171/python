t=int(input())
for i in range(0,t):
    a=int(input())
    A=set(input().split())
    b=int(input())
    B=set(input().split())
    print(A.issubset(B))

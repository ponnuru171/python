s=input("")
W="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r=27
while r>26:
    x=[]
    for i in s:
        x.append(int(i))
        #print(x)
        r=sum(x)
        s=str(r)
        #print(“r=”,r)

if r==0:
    print("Z")
else:
    print(W[r-1])
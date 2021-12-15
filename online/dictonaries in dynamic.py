a=list(input("enter values"))
d=[]
for x in range(len(a)):
    b=input("enter keys")
    d.append(b)
c={ i:j for (i,j) in zip(a,d) }
print("my dictonary is ",c)

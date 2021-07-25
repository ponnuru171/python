x=[1,2,3,4,5,6]
s=[]
for i in x :
    s.append(i**2)
print(s)
def power1(num):
    return(num**2)
s1=list(map(power1,x))
print(s1)

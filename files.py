f=open('f1.txt','r')
#for i in range (0,8):
x=f.readlines()
print(x[0])
x.append("end")
print(x)
    #print(f.readline())
f.close()
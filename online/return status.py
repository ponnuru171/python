key="Alice"
value="online"
statuses = {key:value}
count=0
b=list(statuses.values())
print(b)
for i in range(0,len(statuses)):
    if(b[i] == "online"):
       count=count+1
    else:
        continue
print(count)
a="""Router# show ip interface brief
Interface             IP-Address      OK?    Method Status     	Protocol
GigabitEthernet0/1    unassigned      YES    unset  up         	up
GigabitEthernet0/2    192.168.190.235 YES    unset  up         	up
GigabitEthernet0/3    unassigned      YES    unset  up         	up
TenGigabitEthernet2/1 192.168.193.20  YES    unset  up          up"""
"""[{'interface' : 'GigabitEthernet0/2', 'ip':'192.168.190.235'},{'interface':'TenGigabitEthernet2/1', 'ip':'192.168.193.20'}"""

d=[]
for i in range(len(a)):
    if a[i] == "":
        continue
    else:
        b=d.append(a[i])
c={i:j for i,j in zip(a,d)}
print(c)
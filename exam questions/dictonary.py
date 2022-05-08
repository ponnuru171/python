data = ['Suresh','35', 'Male']
key = ['name','age','gender']
d=[]
res={key[i]:data[i] for i in range(len(data))}
print(res)
print(res.get('age'))
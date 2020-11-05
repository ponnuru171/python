x=range(1,8)
print(list(x))
def even(num):
    if (num % 2) == 0:
        return num
p=list(filter(even,x))
print(p)

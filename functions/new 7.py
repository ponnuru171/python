x=range(-5,10)
print(list(x))
def positive(num):
    if num > 0:
        return num
p1=list(filter(positive,x))
print(p1)
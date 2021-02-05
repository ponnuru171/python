def safe(a,b):
    if a >=0:
        an = pow(a,1/b)
    elif a % 2 == 0:
        an="result is imaginary"
    else:
        an=-(pow((-a),1/b))
    print(an)
    return an
x=safe(2,2)
print(x)

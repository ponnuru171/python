def get_rating(age):
    rating=""
    if age < 18:
        rating="T"
    elif age < 13:
        rating="C"
    elif age == None:
        rating="C"
    else:
        rating="A"
    return rating
x=get_rating(18)
print(x)
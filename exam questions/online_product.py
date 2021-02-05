productidlist=[1,2,3,4,5,6,7,8,9,10]
index=int(input("enter the id for search in list"))
while index<10:
    print(productidlist[index])
    if productidlist == 6:
        break
    else:
        print("id not found")
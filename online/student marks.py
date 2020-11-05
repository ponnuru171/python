x=int(input("enter the number of students" ))
for i in range(0,x):
    y=input("enter student name")
    z=input("enter roll number")
    m1=int(input("enter sub1 marks"))
    m2=int(input("enter sub 2 marks"))
    m3=int(input("enter sub 3 marks"))
    m4=int(input("enter sub 4 marks"))
    tot=m1 + m2 + m3 + m4
    avg=tot / 4
    print("name is", y)
    print("roll number is", z)
    print("total score", tot)
    print("average", avg)
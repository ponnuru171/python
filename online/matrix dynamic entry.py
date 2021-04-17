import numpy as np
a=int(input("enter rows "))
b=int(input("enter columns "))
c=[]
for i in range(a):
   d=[]
   for j in range(b):
       d.append(int(input()))
   c.append(d)
z=np.array(c)
print(z)
print(z.resize((3,1)))

"""# A basic code for matrix input from user

a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))

# Initialize matrix 
c = []
print("Enter the marks" ":")

# For user input 
for i in range(a):  # A for loop for row entries
    d = []
    for j in range(b):  # A for loop for column entries
        d.append(int(input()))
    c.append(d)

# For printing the matrix 
for i in range(a):
    for j in range(b):
        print(c[i][j], end=" ")"""

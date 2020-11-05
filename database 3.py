import sqlite3
conn=sqlite3.connect('test.db')
print("open the database sucessfully")
c=conn.cursor()
#c.execute("create table products(pname text(10),pbrand text(10),pprice number(10))")
c.execute("insert into products values('good day','britaneya',20)")
c.execute("insert into products values('bru','neskefe',80)")
c.execute("insert into products values('voltas','ac',40000)")
conn.commit()
c.execute("update products set pbrand='aircondition' where pname='voltas'")
c.execute("select * from products")
data=c.fetchall()
for row in data:
    print(row)

import sqlite3
conn=sqlite3.connect('test.db')
print("open database sucessfully")
c=conn.cursor()
def creat():
    c.execute("create table laptop(lname text(10),lram text(10),lprocessor text(10),lbattery number(20))")
def insert():
    c.execute("insert into laptop values('dell','4gb','i7 5g',12000)")
    c.execute("insert into laptop values('hp','8gb','i5 10g',12500)")
    c.execute("insert into laptop values('lenovo','16gb','i3 10g',13000)")
    conn.commit()
def select():
    c.execute("select * from laptop")
    data=c.fetchall()
    for row in data:
        print(row)
#creat()
insert()
select()
c.close()
conn.close()

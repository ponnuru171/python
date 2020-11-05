import sqlite3
conn=sqlite3.connect('test.db')
print("open database sucessfully")
c=conn.cursor()
def create():
    c.execute("create table site (sname text(10),sarea number(20))")
def insert():
    c.execute("insert into site values('balaji nagar',1200)")
    c.execute("insert into site values('himayath nagar',2300)")
    conn.commit()
def select():
    c.execute("select * from site")
    data=c.fetchall()
    for row in data:
        print(row)
#create()
insert()
select()
c.close()
conn.close()

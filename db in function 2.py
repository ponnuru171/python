import sqlite3
conn=sqlite3.connect('test.db')
print("open dtabase sucessfully")
c=conn.cursor()
def creat():
    c.execute("create table humans(hname text(10),hage number(5),hvitamins text(10),hdeficiency text(20))")
def insert():
    c.execute("insert into humans values('sai',21,'a','eye site')")
    c.execute("insert into humans values('srinu',21,'b','anemia')")
    conn.commit()
def layout():
    c.execute("select * from humans")
    data=c.fetchall()
    for row in data:
        print(row)
#creat()
insert()
layout()
c.close()
conn.close()

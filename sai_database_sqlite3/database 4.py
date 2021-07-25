import sqlite3
conn=sqlite3.connect('test.db')
print("open the database sucessfully")
c=conn.cursor()
#c.execute("create table human(hname text(10),hage number(10),hvitamin text(10),hdefeciency text(10))")
c.execute("insert into human values ('sai',21,'b','animea')")
c.execute("insert into human values ('srinu',21,'a','eye site')")
c.execute("insert into human values ('chandu',21,'c','internal bleeding')")
c.execute("insert into human values ('harsha',21,'d','rickets')")
conn.commit()
c.execute("update human set hage=20 where hname='sai'")
c.execute("select * from human")
data=c.fetchall()
for row in data:
    print(row)
c.close()
conn.close()


import sqlite3
conn=sqlite3.connect('test.db')
print('opened database sucessfully')
c=conn.cursor()
#c.execute('create table student(sname text(10),sid text(10))')
c.execute("insert into student values('venkata','9916005171')")
c.execute("insert into student values('venkata 1','9916005174')")
c.execute("insert into student values('venkata 2','9916005176')")
conn.commit()
c.execute("select * from student")
data=c.fetchall()
for row in data:
    print(row)
c.close()
conn.close()
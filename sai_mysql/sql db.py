import mysql.connector
conn=mysql.connector.connect(host='localhost',database='db1',user='root',password='India12345')
c=conn.cursor()
c.execute("create table student(sname varchar(10),sid integer(10))")
c.execute("insert into student values('sai',123456)")
conn.commit()
c.execute("select * from student")
data=c.fetchall()
for row in data:
    print(row)
c.close()
conn.close()

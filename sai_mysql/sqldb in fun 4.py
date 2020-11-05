import mysql.connector
conn=mysql.connector.connect(host='localhost',database='db1',username='root',password='India12345')
c=conn.cursor()
def create():
    c.execute("create table human(hname varchar(10),hdisease varchar(19),hcure varchar(20))")
def insert():
    c.execute("insert into human values('sai','eyesite','vitamin A')")
    c.execute("insert into human values('srinivas','asthama','inheller')")
    c.execute("insert into human values('chandu','less blood','vitamin k')")
    conn.commit()
def select():
    c.execute("select * from human")
    data=c.fetchall()
    for row in data:
        print(row)
#create()
insert()
select()
c.close()
conn.close()
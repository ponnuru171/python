import mysql.connector
conn=mysql.connector.connect(host='localhost',database='db1',username='root',password='India12345')
c=conn.cursor()
def creat():
    c.execute("create table car(cname varchar(15),cmilage varchar(10),cprice integer(10))")
def insert():
    c.execute("insert into car values('honda','40k',1300000)")
    c.execute("insert into car values('audi','35k',3500000)")
    c.execute("insert into car values('rolls royals','20',100000000)")
    c.execute("insert into car values('benz','35k',4000000)")
    conn.commit()
def select():
    c.execute("select * from car")
    data=c.fetchall()
    for row in data:
        print(row)
#creat()
insert()
select()
c.close()
conn.close()
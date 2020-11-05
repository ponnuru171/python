import mysql.connector
conn=mysql.connector.connect(host='localhost',database='db1',username='root',password='India12345')
c=conn.cursor()
def create():
    c.execute("create table product(pname varchar(20),pbrand varchar(10),pbatchno integer(10),pprice integer(10))")
def insert():
    c.execute("insert into product values('johnsons baby','wipro',123478,70)")
    c.execute("insert into product values('5 star','catbury',234567,20)")
    c.execute("insert into product values('diary milk','catbury',345678,20)")
    c.execute("insert into product values('annapurnam atta','pills',156789,60)")
    conn.commit()
def select():
    c.execute("select * from product")
    data=c.fetchall()
    for row in data:
        print(row)
#create()
insert()
select()
c.close()
conn.close()

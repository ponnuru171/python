import mysql.connector
conn=mysql.connector.connect(host='localhost',database='db1',username='root',password='India12345')
c=conn.cursor()
def create():
    c.execute("create table employee(ename varchar(10),edepartment varchar(20),esalary integer(10),eid integer(10))")
def insert():
    c.execute("insert into employee values('srinivas','sales',20000,1234789)")
    c.execute("insert into employee values('chandu','manager',25000,1345678)")
    c.execute("insert into employee values('ganesh','production',23000,23456789)")
    c.execute("insert into employee values('venkata','HR',30000,12367890)")
    conn.commit()
def select():
    c.execute("select * from employee")
    data=c.fetchall()
    for row in data:
        print(row)
#create()
insert()
select()
c.close()
conn.close()

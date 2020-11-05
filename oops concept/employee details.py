class employee:
    def details(self,name,id,salary,department):
        self.name=name
        self.id=id
        self.salary=salary
        self.department=department
    def info(self):
        print(self.name + " is working as " +str(self.department) + " from lasst year")
    def pay(self):
        print(self.id , " is having a salary " , self.salary, " without increment")
    def increment(self):
        self.salary = self.salary + ((self.salary) * (20/100))
        print("increment salary is " ,self.salary)
e= employee()
e.details("sai",9347678014,20000,"HR")
e.info()
e.pay()
e.increment()
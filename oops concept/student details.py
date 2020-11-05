class students:
    def details(self,name,age,regno,total):
        self.name=name
        self.age=age
        self.regno=regno
        self.total=total
    def info(self):
        print(self.name + " is " + str(self.age) + " years old. ")
    def marks(self):
        print(self.regno + " has gained total is " + str(self.total)  + " ")
    def result(self):
        print("results for student")
s = students()
s.result()
s.details("ravi",21,"9916005171",7.9)
s.info()
s.marks()
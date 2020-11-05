class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
o = Dog("Ozzy", 2)
s = Dog("Skippy", 12)
f = Dog("Filou", 8)
o.doginfo()
s.doginfo()
f.doginfo()
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("the name is {},the age is {}".format(name,age))

    def bark(self):
        print("bark bark!")
c=Dog("sam",12)
c.bark()
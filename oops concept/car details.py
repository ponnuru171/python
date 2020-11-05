class cars:
    def details(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def info(self):
        print(self.name + " car having a model " + str(self.model) + " having a price ", self.price)
    def cost(self):
        if (self.model < 2010):
            x = (self.price) * (20/100)
           # print("you get the discount of ",self.price)
            self.price = (self.price) -((self.price) * (20 / 100))
            print("the detertion valus is ",x)
            print("the final cost will be",self.price)
        else:
            print("there is no discount in the price final cost is ", self.price)
c=cars()
c.details("Auddi",2009,15000000)
c.info()
c.cost()
class Food: #base class
    """ init__() method: This is the constructor method of the Food class.
    It gets called automatically when an object of the Food class is created. 
    It takes name and price as arguments and assigns them to the object's attributes (self.name and self.price). """
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print(f"{name} is created from base class")

    def eat(self):
        print("eat method from base class")
class Apple(Food): #derived class
    def __init__(self, name,price,amount):
        #Food.__init__(self,name)#create instance from base class
        """ super().__init__(name, price): This line calls the __init__() method of the base class Food.
        This ensures that the name and price attributes are initialized properly in the base class. """
        super().__init__(name,price)        
        # self.name=name # without it will give when creating object from apple class that: (apple object has no attribute name)
                         #which mean that it does not inhirit the name from base class Food
                         # instead of writing this (self.name=name) write Food.__init__(self,name) because 
                         # def __init__(self, name):=> override on inheritance of parent init
        self.amount=amount                 
        print(f"{self.name} is created from derived class and price is {self.price} and amount is {self.amount}")
    #this represent method overriding any object from the apple class when calling eat method would call from son not parent
    def eat(self):
        print("eat method from derived class")    
    def get_from_tree(self):
        print("get from tree from derived class")    
""" Step 1: The Apple class's __init__() method is called.
    Step 2: Inside Apple's __init__(), super().__init__(name, price) is executed,
    which calls the __init__() method of the base class Food. 
    This initializes the name and price attributes in the Food class 
    Step 3: After returning from the base class's __init__() method,
    the Apple class's __init__() method continues executing
    """
food_two=Apple("pizza",500,30.2) 
                        #pizza is created from base class
                        #pizza is created from derived class
                        
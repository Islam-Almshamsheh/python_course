# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:
    def __init__(self):
        print("Base One")

    def func_one(self):
        print("One")
    def __str__(self):
        return "welcome from base one"

class BaseTwo:
    def __init__(self):
        print("Base Two")

    def func_two(self):
        print("Two")
    def __str__(self):
        return "welcome from base two"

class Derived(BaseOne, BaseTwo):
    pass


my_var = Derived() #Base One:because its inherit from baseone at first based on mro()
""" this method return object its type method resolution order 
    shows the order of the base classes
"""
# print(Derived.mro())

print(my_var)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()


class Base:
    pass


class DerivedOne(Base):
    pass


class DerivedTwo(DerivedOne):# will inherit from both Base & DerivedOne
    pass 
# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism -- => many_forms
# -------------------------------------------------
#same method perform different actions at differen locations
n1 = 10
n2 = 20

print(n1 + n2) #perform addition

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2) #perform cocatination

print(len([1, 2, 3, 4, 5, 6])) #word on list => count the elements
print(len("Osama Elzero")) #word on string =>count the letters
print(len({"Key_One": 1, "Key_Two": 2})) #word on tuple => count only the keys


class A:
    def do_something(self):
        print("From Class A")
        raise NotImplementedError("Derived Class Must Implement This Method")


class B(A):
    def do_something(self):
        print("From Class B")


class C(A):
    def do_something(self):
        print("From Class C")


my_instance = B()
my_instance.do_something()
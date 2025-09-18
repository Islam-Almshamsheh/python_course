# ----------------------------------------------------------------------------------------
# -------------- Object Oriented Programming => ABCs => Abstract Base Class --------------
# ----------------------------------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# ----------------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

    @abstractmethod
    def has_name(self):
        pass


class Python(Programming):
    def has_oop(self):
        return "Yes"


class Pascal(Programming):
    def has_oop(self):
        return "No" # if i replace the return with pass it will give None as a result 
                    # if i removed the entier func. has_opp will give =>
                    #  TypeError:Can't instantiate abstract class Pascal without an implementation for abstract method 'has_oop'

    def has_name(self):
        return "Pascal"


one = Pascal()

print(one.has_oop())
print(one.has_name())

# implementing of abstract method in derived class can considered as overriding?
# in both it should be inheritance, but overridding in the base class there is an implementation
# and there is no restriction on implementing this method in the derived class 
""" Abstract Methods Have No Implementation: Unlike regular method overriding,
    where the base class may have a method with an implementation that the derived class overrides,
    abstract methods have no implementation in the base class, and the abstract method is like a contract must be
    (instantiat)/fulfill by the derived class.
    They are purely a specification.  """
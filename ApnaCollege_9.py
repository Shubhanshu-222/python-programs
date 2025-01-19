# del keyword
# used to delete object properties or object itself

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shubhanshu")
print(s1.name)
del s1.name
#print(s1.name) # This sentence will give error as s1.name been deleted


# Private attributes & methods

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # Adding two under scores will make it private

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "12345_pass")

print(acc1.acc_no)
# print(acc1.__acc_pass) # This will give error as acc_pass is private. We are unable to access it outside class

acc1.reset_pass() # This will print the acc_pass as the method has access to the variable.


class Person:
    __name = "anonymous" # This is a private variable

    def __hello(self): # This will make the function private
        print("Hello Person!")
    
    # This private function but can be used by another function in the class

    def welcome(self): # This method call can be made as shown in line 47
        self.__hello() 


p1 = Person()
# print(p1.__name) # This will give error as the variable is private
# p1.__hello() # This will also give error as the function is private so cannot be called this way
p1.welcome()


# Inheritance
# when one class derives the properties and methods of another class (parent/base).

class Car: # Parent class
    pass

class ToyotaCar(Car): # Derived class
    pass

# Inheritance types - Single, Multi-level, Multiple
# Single - base - derived
# Multi-level - base - derived (new base) - new derived -> This can have many levels
# Multiple - base1 - base2 - derived

# Super method - used to access methods of the parent class

class Cars:
    def __init__(self, type):
        self.type = type

    @staticmethod # This means that for each new instance or object, this method will not get created again but will be created once and will be common/shared for all instances/objects.
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCars(Cars):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCars("Prius", "Electric")
print(car1.type)


# Class method - It is bound to the class and receives the class as an implicit first argument
# Static method cant access or modify class state
# class attributes are changed using class methods and not static methods.
# use @classmethod decorator

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Shubhanshu")
print(p1.name)
print(Person.name)


# Three types of functions - static methods, class methods (cls), instance methods (self)


# Property decorator - it is used in the class to use the method as a property
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math)/3) + "%"


    # def calcPercentage(self):
        # self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"


stu1 = Student(98, 99, 100)
print(stu1.percentage)

# by using property, changes are reflected automatically, otherwise it doesnt


# Polymorphism : Operator Overloading - 40:00
# when the same operator is allowed to have different meaning as per context
# getter and setter decorator (other decorators to study)

# for eg + operator. For int it adds, for string it concatenates and for list it merges them
# so when we create our class, we can do the same thing with it.

# complex numbers are used in voice recognition. Very important topic - Voice recognition in machine learning.

class Complex:
    def __init__(self, real, img): # This is also a dunder function. Check other in-built dunder function in Python documentation
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

# Operators and Dunder functions
# double underscore before a function makes the function a dunder function
# __add__
    
    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

num3 = num1 + num2 # This is not possible in Python but this logic can be created
num3.showNumber()

num4 = num1 - num2
num4.showNumber()


# Practice Question 59:00
# 


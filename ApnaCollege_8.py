#OOPS - Object Oriented Programming Principles

# creating class - class is a blueprint for creating objects
class Student:
    name = "Shubhanshu Bansod"

class Car:
    color = "blue"
    brand = "BMW"

# creating object
s1 = Student()
print(s1.name)

c1 = Car()
print(c1.color)
print(c1.brand)

# _ _init_ _ function 
# Constructor - all classes have a function called _init_(),
# this function is always executed when the object is being initiated
# python automatically creates one, we write one or not
# () these brackets are put to call the constructor

class City:
    def __init__(self, cityname):
        self.name = cityname
        print(self)
        print("adding new city in database..")

# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.

city1 = City("Nagpur");
print(city1.name)


class Students:
    
    # __init__ default constructor
    def __init__(self):
        pass

    # __init__ here is a parameterized constructor
    def  __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database")

s3 = Students("Shubhanshu", 49)
print(s3.name, s3.marks)

s4 = Students("Prajakta", 35)
print(s4.name, s4.marks)

# if we dont make the default constructor, python will create it by default
# but usually we keep only constructor

# Class & Instance attributes
# self.name and marks are instance attributes
# a repeated variable is made class attribute so it stays same for all related objects, it saves memory
# object attribute precedence higher than class attribute, in case both variable name is same

# Methods
# these are functions which belong to the class/object.

class Studentss:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome student!")

    def get_marks(self):
        return self.marks

s5 = Studentss("Pranjal", 97)
s5.welcome()
print(s5.get_marks())


# Practice question 35:00
# Create student class that takes name and and marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Students3:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,", self.name, "your average score is", sum/3)

s1 = Students3("Shubhanshu Bansod", [99, 89, 79])
s1.get_avg()

s1.name = "Tony Stark"
s1.get_avg()


# Static Methods
# These methods dont have self parameter and work at class level
# use decorator @staticmethod
# It changes the behaviour of the method

class Student4:
    def __init__(self):
        pass

    @staticmethod
    def college():
        print("ABC College")


# Four pillars of OOP
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# Abstraction - hiding the implementation details of the class and
# only showing the essential features to the user

class Vehicle:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Vehicle has started")

car1 = Vehicle()
car1.start()


# Encapsulation
# it means wrapping data and functions into a single unit (object).
# all code written in this file can be called encapsulation.


# Practice question 49:00
# Create Account class with 2 attributes - balance & account no
# Create methods for debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, " was debited.")
        print("Total balance = ", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, " was credited.")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)

acc1.debit(5000)
acc1.credit(10000)
        
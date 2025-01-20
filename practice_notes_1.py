#first program
print("First Program written by Shubhanshu")

name = "Shubhanshu"
age = 22
print("My name is: ", name)
print("My age is: ", age)

print(type(name))
print(type(age))
#Data types: Integers, String, Float, Boolean, None

#Types of operators: Arithmetic, Relational/Comparison
# Assignment, Logical

#Type conversion
# conversion and casting
# conversion happens automatically, casting is manual
a = 2 #int type
b = 4.25 #float type
sum = a+b #sum gets automatically converted to float
print(sum)

a = "2" #string
b = 4.25 #float
sum = int(a) + b #a gets manually converted
print(sum)

#cant convert chararter string to int or float

a = 3.14
a = str(a) #converting number to string
print(type(a))

#Taking user input
name = input("Enter your name: ")
print("Welcome", name)

#for numbers, need to perform casting on input as input always returns a string
val = int(input("Enter a value: "))
print(type(val))

#Program to input side of square and print its area
#Program to input two floating point numbers and print their average
#Program to input two numbers and print True if a>=b else print False

#Functions and Recursion

#Function - block of statements that perform a specific task
#used to reduce redundancy in programs
"""function declaration and definition
def func_name(param1, param2...):
    some work
    return val
"""
"""function call
func_name(arg1, arg2...)
"""
def calc_sum(a, b):
    return a+b

print("Sum of 4 and 5 is", calc_sum(4,5))

#a function which doesn't returns anything will by default return None.
def print_hello():
    print("Hello")

text = print_hello() #this will save None in text as the function returns None
print(text) #this will print None

#types - built-in function, user defined function
#built-in -> print, len, type, range
#user-defined -> calc_sum

#default parameters - parameters which are used when no argument is passed during function call
#these parameters are set by the coder in function definition
""" def cal_prod(a=1,b=1):
        return a*b
"""
#note: non-default parameters should be always be placed before default arguments
""" def cal_prod(a, b=2):
        here a is non-default, and b is default
"""

#Programs 21:30
#Program to print the length of a list. Here, list is a parameter.
#Program to print the element of a list in a single line.
#Program to find the factorial of n.
#Program to convert USD to INR.


#Recursion - when a function calls itself repeatedly
#print n to 1 backwards
def reverse(a):
    print(a)
    if(a==1):  #base case is very important in recursion
        return #controlled return
    reverse(a-1)
reverse(10)

#factorial
def calc_fact(a):
    if(a==1 or a==0):
        return 1
    else:
        return calc_fact(a-1)*a #Recurrence Relation

print("Factorial of 5 is", calc_fact(5))

#Programs 55:10
#Program to calculate the sum of first n natural numbers  using recursive function.
#Program to print all elements in a list using a recursive function. Using list and index as parameters.

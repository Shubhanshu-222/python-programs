# Program to input side of square and print its area
side = int(input("Enter side of a square (cms):"))
area = side*side
print("Area of the square is:", area)

#Program to input two floating point numbers and print their average
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Average of the numbers is", (a+b)/2)

#Program to input two numbers and print True if a>=b else print False
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("a>=b:", a>=b)

#Program to input user's first name and print its length
str_name = input("Enter your name: ")
print("The length of the string is", len(str_name))

#Program to find the occurence of '$' in a string
#Program to check if a number entered by the user is odd or even
num = int(input("Enter a number:"))
if(num%2 == 0):
    print("Number is even!")
else:
    print("Number is odd!")

#Program to find the greatest of 3 numbers entered by the user
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if(num1>num2 & num1>num3):
        print("First number is greatest!")
elif(num2>num1 & num2>num3):
        print("Second number is greatest!")
else:
        print("Third number is greatest!")

#Program to check if a number is a multiple of 7 or not
#(very easy num%7 == 0)

#Program to ask the user to enter names of thier 3 favorite movies & store them in a list
movies = []
movies.append(input("Enter your first favourite movie:"))
movies.append(input("Enter your second favourite movie:"))
movies.append(input("Enter your third favourite movie:"))
print(movies)
    
#Program to check if a list contains a palindrome of elements
list1 = ["a", "b", "c", "d", "d", "c", "b", "a"]
copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("Palindrome List!")
else:
    print("Not Palindrome List!")


#Program to count the number of students with "A" grade in the following tuple
# ["C", "D", "A", "A", "B", "B", "A"]

#Store the above values in a list and sort them from "A" to "D"

#Program to print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)

#Program to search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100)
nums = [1,4,9,16,25,36,49,64,81,100]
x = 36
idx = 0
for i in nums:
    if(i==x):
        print("Number found at index", idx)
    else:
        print("Searching...")
    idx += 1

#Program to find the sum of first n numbers.
#using While loop
sum = 0
n = int(input("Please enter a number: "))
i = 0

while(i<=n):
    sum = sum+i
    i += 1

print("Sum of numbers till", n, "is", sum)

#using for loop
sum = 0
n = int(input("Please enter a number: "))

for i in range(n+1):
    sum = sum+i

print("Sum of numbers till", n, "is", sum)

#Program to find the factorial of first n numbers.
#using while loop
factorial = 1
n = int(input("Please enter a number: "))
i = 1

while(i<=n):
    factorial = factorial*i
    i += 1

print("Factorial of", n, "is", factorial)

#using for loop
factorial = 1
n = int(input("Please enter a number: "))


for i in range(1, n+1): #need to give starting num else it will start from 0 
    factorial = factorial*i

print("Factorial of", n, "is", factorial)

#Program to print the length of a list. Here, list is a parameter.
#Program to print the element of a list in a single line.
#Program to convert USD to INR.

#Program to calculate the sum of first n natural numbers  using recursive function.
#Program to print all elements in a list using a recursive function. Using list and index as parameters.

"""
Program to create a new file "practice.txt" using python. Add the following data in it:

Program to replace all occurences of "java" with "python" in above file
Program to search if the word "learning" exists in the file or not
"""
#first one
with open("test2.txt", "w") as f:
    f.write("Hi Shubhanshu, please learn\nJava well.\n")
    f.write("Please be efficient in Java asap!")

f.close()

#second one
with open("test2.txt", "r") as f:
    data = f.read()
new_data = data.replace("Java", "Python")
print(new_data)

with open("test2.txt", "w") as f:
    f.write(new_data)

#third one
word = "Shubhanshu"
with open("test2.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found!")


# Write a function to find in which line of the file does the word "learning" occur first. Print -1 if word not found.
def check_for_line():
    word = "Please"
    data = True
    line_no = 1
    with open("test2.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

check_for_line()


# Print the count of even numbers from a file containing numbers separated by comma.
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

"""
steps: 1) take out individual numbers
2) parse/casting to int
"""
# without using split method
num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]

# using split method
count = 0
nums1 = data.split(",")
print(nums1)
for val in nums1:
    if(int(val) % 2 == 0):
        count += 1
print(count)

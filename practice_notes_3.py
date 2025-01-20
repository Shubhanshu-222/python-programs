#List and Tuple in Python - sort of equivalent to arrays

#list
marks=[94.4, 87.5, 77, 65.45, 50]
print(marks)
print(type(marks)) 

#it has indexing which can be used to access the elements
print(marks[0])
print(marks[2])
print(len(marks)) #will show the length of list

#we can store elements of different types together in one list
student = ["Shubhanshu", 22, "Grade A", 99.5]
print(student)

#Strings are immutable in Python - VERY IMPORTANT
#and List are mutable, therefore strings can be updated in List
student[0] = "Prajakta"
print(student)

#List Slicing - similar to string slicing
#list_name[starting index: ending index]
marks = [91, 55, 63, 36, 47, 20, 12, 15, 78, 100]
print(marks[4:8]) #works just like string slicing

#Slicing based on Negative indexing can also be done in List

#List Methods - append, sort {ascending, descending}, reverse, insert
marks.append(5)
print(marks)

marks.sort() #in ascending by default, returns None value so cannot use 'marks = marks.sort()'
#also will print None if print(marks.sort()) is used
print(marks)

marks.sort(reverse = True) #to print in reverse
print(marks)
#sorting possible in strings

marks.reverse()
print(marks)

marks.insert(2, 100) #inserts 100 at index 1 and shifts all the elements including previous element at index 1 to right side.
#insert(index, value)
print(marks)

marks.remove(100) #removes the first occurence of element
print(marks)
marks.pop(3) #removes element at given index
print(marks)
#and many other methods - take your time


#tuple
#works almost like list but tuple creates immutable sequence of values
#while list creates mutable sequence of values
#to convert list into tuple, just chaange square brackets to round brackets

#List -> marks = [values]
#Tuple -> marks = (values)

marks_tup = (94.4, 87.5, 77, 65.45, 50)
print(type(marks_tup))

#marks1[4] = 34 this assignment operation is not allowed

#can create empty tuple like, marks = ()
#can create single value tuple like, marks = (45,)
#comma is compulsory else type will change to integer.

print(marks_tup[1:3])

#Tuple methods
print(marks_tup.index(77)) #returns index of first occurence

print(marks_tup.count(77)) #counts total occurrences

#Program to ask the user to enter names of their 3 favorite movies & store them in a list
#Program to check if a list contains a palindrome of elements
#Program to count the number of students with "A" grade in the following tuple
# ["C", "D", "A", "A", "B", "B", "A"]

#Store the above values in a list and sort them from "A" to "D"
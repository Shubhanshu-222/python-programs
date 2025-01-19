#Loops

#while loop
count = 1 #iterator
while count<5 :
    print("I love you very much, Bokya!")
    count += 1

#Programs @ 19:45
# Program to print the elements of the following list using a loop:
# Program to search a number x in this tuple using loop

#break and continue

#for Loops - used for sequential traversal. So, for traversing list, string, tuples etc
# for element in list:
#    print(element)
nums = [1,2,3,4,"Apple","Banana"]
for val in nums:
    print(val) #traversing list

#can be used with tuple, string as well

str = "Shubhanshu"
for i in str:
    print(i) #traversing string

#for loop with else
#else block of code executes when loop ends
"""for element in list:
        some work
    else:
        work when loop completely runs till last iteration
"""
#else used in specific cases where we use break
#code in else wont run if the code breaks out in between

#Programs @ 43:30
#Program to print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]
#Program to search for a number x in this tuple using loop:
# (1,4,9,16,25,36,49,64,81,100) - This is a Linear Search

#range() - Range function, returns sequence of number, starts from 0, step size by how much it increments
#ending number is not included

# range(10) -> range(stop at 10)
# range(2, 10) -> range(start at 2, stop at 10)
# range(2, 10, 2) -> range(start at 2. stop at 10, increment by 2)

for i in range(2,10):
    print(i)

for i in range(2,100,2): #will print even numbers
    print(i)

for i in range(1,100,2): #will print odd numbers
    print(i)

#step size can be negative as well
for i in range(100, 0, -1):
    print(i)

#pass Statement - It is a null statement that does nothing.
#It is used as a placeholder for future code. Else will result in error

#Program to find the sum of first n numbers.
#Program to find the factorial of first n numbers.



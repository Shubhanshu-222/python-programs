# \n is new line. \t is tab space
str1 = "A very good morning.\nMy name is Shubhanshu.\tAnd I live in Mumbai"
print(str1)

str2 = "\nI love someone very much!"

final_str = str1 + " " + str2 #concatenation. The space in middle is optional.
print(final_str)

#length of str
print(len(final_str))

#Indexing. It means all characters in a string
#gets an index. It starts from 0.
#We can use index to get a specific character from string

str3 = "Shubhanshu"
ch = str3[0]
print(ch)

#But we cannot change the character using index
#It gives error. So, we can only access it.

#Slicing = accessing parts of a string
#str[starting index : ending index]
print(str3[2:8])
print(str3[:4]) #Python auto fills the starting index as 0
print(str3[5:]) #Python auto fills the ending index as last char

#Negative index
print("Negative Index:")
print(str3[-7:-1])

#String Functions
#endswith, capitalize, replace, find, count
#learn other functions as well

#Program to input user's first name and print its length
#Program to find the occurrence of '$' in a string

#Conditional Statements
#if-elif-else
#nesting

#Program to check if a number entered by the user is odd or even
#Program to find the greatest of 3 numbers entered by the user
#Program to check if a number is a multiple of 7 or not


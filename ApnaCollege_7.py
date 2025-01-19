#File I/O
#text files: .txt, .docx, .log etc
#binary files: .mp4, .mov, .png, .jpeg etc

#Open, read and close file
"""
f = open("file_name","mode")
data = f.read()  # mode r: read mode, w: write mode
f.close()

"""

f = open("test.txt", "r")
data = f.read()
print(data)
print(type(data))

f.seek(0) #move the file pointer back to the beginning of the file
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)

# to write in a file, open file using w or a mode
# in w and a mode, the file if not present will get auto created.

f.write("\nI want to go to NASA.")

# to read and write from the start of the file use r+
# in w+, the file gets wiped out/truncated

f.close()

# with Syntax
"""
with open("text.txt", "a") as f:    #f is an alias
    data = f.read()
    
"""

# deleting a file. using os module. need to install module if not installed using pip

# practice questions 33:00
"""
Program to create a new file "practice.txt" using python. Add the following data in it:

Program to replace all occurrences of "java" with "python" in above file
Program to search if the word "learning" exists in the file or not
""" 
#practice questions 39:15
# Write a function to find in which line of the file does the word "learning" occur first. Print -1 if word not found.

# Print the count of even numbers from a file containing numbers separated by comma.




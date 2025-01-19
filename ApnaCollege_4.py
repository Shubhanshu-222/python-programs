#Dictionary and Sets - built in data sets and very important data structure

#Dictionary - used to store data in key:value pairs
#These are unordered, mutable and dont allow duplicate keys

myInfo = {
    "key" : "value",
    "name" : "Shubhanshu",
    "age" : 22,
    "job" : "student",
    "is_adult" : True,
    "likes" : ["list", "music", "writing", "eating maybe"],
    "hobbies" : ("tuple", "had", "dont have any", 10),
    5 : "Can use integers as keys",
    10.55 : "Can use floats as keys"
}
#can also make tuple keys as they are immutable

print(type(myInfo))

#To access values of dictionary - use keys instead of index as there are no indexes
print(myInfo["name"])
print(myInfo["likes"])
print(myInfo["hobbies"])

myInfo["name"] = "Shubhanshu Bansod" #will overwrite. can also put number
print(myInfo["name"])

#null dictionary
null_dict = {}
null_dict["name"] = "Prajakta"
print(null_dict)

#Nested dictionaries - can create a dictionary in place of value
student = {
    "name" : "Shubhanshu Bansod",
    "marks" : {
        "Maths" : 100,
        "OS" : 100,
        "SEPM" : 100
    }
}
print(student)
print(student["marks"]["Maths"])

#Dictionary methods - keys, values, items, get, update

#keys - returns all keys
print(student.keys())
print(list(student.keys())) #to typecast into List
print(len(student.keys())) #to find out length

#values - returns all values
print(student.values())
print(list(student.values())) #to convert into list
#so we can store dictionary inside list and vice-versa

#items - returns all (key, val) pairs as tuples
print(student.items())
pairs = list(student.items()) #type casted to list
print(pairs[0]) #first tuple in list
print(pairs[1]) #second tuple in list

#get - returns the value according to key
print(student["name"]) #if wrong key is put, gives error
print(student.get("name")) #if wrong key is put, gives no error but prints None
#if error occurs, code lines after the error line wont get executed.
#Very Important - An error should never stop the code as in real scenario it will mean that your webpage will stop working if an error occurs

#update - inserts the specified items to the dictionary
#dict.update(key:value)
student.update({"city" : "Mumbai"})
print(student)
student.update({"city" : "Mumbai", "lover" : "Prajakta"})
#if already existing key is passed then the value gets updated instead


#Sets
#collection of unordered items
#each element must be unique and immutable. Set is mutable though.
#cannot store mutable elements in sets like list and dictionary as elements needs to be immutable
#but can store - boolean, int, floar, string, tuple
#in set, only values are stored.

first_set = {"Shubhanshu", 22, "Prajakta", 21}
print(type(first_set))

#duplicate values are ignored and only one is saved
#repeated print of sets will show values in different order. So sets are unordered

#empty set 
# collection = {} - empty dictionary
collection = set()
print(type(collection))

#Set methods - add, remove, clear, pop
#add - adds an element
collection.add("Hi")
collection.add(22)
collection.add((4, 5, 9)) #this is tuple added in the set
#collection.add([6, 7, 10]) - this is a list and will give TypeError: unhashable type
#immutable values are hashable values. unhashable means whose values can change i.e. mutable

#remove - removes the element
collection.remove(22)
#will give error if any element not is set is entered

#clear - empties the set
collection.clear()
print(len(collection))

#pop - removes a random value
collection = {"Shubhanshu", "Prajakta", "Random1", "Random2"}
collection.pop()
print(collection)
collection.pop()
print(collection)
collection.pop()
print(collection)
collection.pop()
print(collection)

#Set important methods - union, intersection
#set.union(set2) - combines both set values and returns new
#so all the values without duplicated values, will get combined


#set.intersection(set2) - combines common values and returns new
#self explanatory

#Programs 43:00 onwards
#Program to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value
#Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
# values = {9, "9.0"} or {"9", 9.0}
"""values = {
    ("float", 9.0),
    ("int", 9)
}""" #These are pairs in the form of tuples
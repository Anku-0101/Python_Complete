'''
Python Lists are containers to store a set of values of any data type.
friends = ["Apple", 'M', 5, 3.5, False]

List Indexing 
A list is indexed just like a string 
'''
a = ['a','b','c']
print(a)
print(a[-1])
print(a[2])

# Create a list using []
# Print the list using print() function 

#List Slicing 
friends = ["Aman", "Shivam", "Abhishek", 34, 'P', 7.2]
friends[0] = 5 # Lists are mutable data types 
print(friends[0:4])
print(friends[-4:])
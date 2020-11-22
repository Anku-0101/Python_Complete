# Dictionary is a collection of key-value pairs
'''
Properties of a Python Dictionaries
1. It is unordered
2. It is mutable
3. It is indexed
4. Cannot Contain duplicate keys
'''

myDict = {
    "Fast" : "In a quick manner",
    "Aman" : "A student",
    "Five" : 5,
    "Marks" : [1,2,7,8],
    "AnotherDict" : 
    {
        'Harry' : 98,
        'Six'   : 6,
        "Amazon" : "discount"
    }
}

print(myDict['Fast'])
print(myDict['Aman'])
print(myDict['Five'])
print(myDict['AnotherDict']['Amazon'])


#List Methods

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
    },
    5 : 7
}

print(myDict.keys()) # Print the keys of the dictionary
print(type(myDict.keys())) # Type of keys is not list
print(list(myDict.keys())) # casting the types to list
print(myDict.values()) # Outputs the value of the Dictionary
print(myDict.items()) # Print the (key, value) for all contents of the dictionary

updateDict = {
    "Verma" : "Subham",
    "Sekhar" : "Suman",
    "Divya" : "Bharti",
    "Fast" : "Quick"
}

myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)


# The difference between .get and [] syntax in Dictionaries
print(myDict.get("Keys")) # Returns None as keys is not present in the dictionary, avoids error
# print(myDict["Keys"]) # throws an error as Keys is not present in dictionary
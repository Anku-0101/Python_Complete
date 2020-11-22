# Declaring an empty set 
b = [19, 14, 86]
a = set(b)

#adding elements to a set 
a.add(2)
a.add(5)
a.add(4)

# a.add([7,5,6]) # Can't add hashable type i.e list to a set
# b.add({4:5}) #Cannot add list or dictionary to sets 

# Tuples can be added to sets
a.add((9, 44, 7))
print(a)




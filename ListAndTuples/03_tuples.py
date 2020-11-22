# Creating a tuple using ()
t = (1,2,6,4,0,7)

# Printing the elements of a tuple
print(t[0])

# Cannot update the values of a tuple, both tuple and string are immutable data type
# once defined a tuple element cannot be altered or manipulated 

# t[0] = 74 
# abc = "Amazing"
# abc[1] = 'a'
# print(abc)

t1 = () #Empty tuple
print(t1)

# Wrong way to declare a tuple with single element, 
# in this way of declaration t1 will be an integer value having value 1
t2 = (1) 
print(t2)

t3 = (1,)
print(t3)
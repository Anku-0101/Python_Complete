'''
Properties of Sets
1. Sets are unordered => Elements' order doesn't matter
2. Sets are unindexed => Can't access elements by index
3. There is no way to change items in sets
4. Sets cannot contain duplicate values 

'''

#Operations on Sets 

s = {1, 3, 5, 7, 2, 3, 1, 4}

print(len(s)) # Print the length of this set
print(s)
s.remove(7) # Removes 7 from the set, throws an error if the element is not present in the set
print(s)

print(s.pop()) # Removes an arbitary element from the set and return the element removed 
print(s)
s.clear() # Empties the set s
print(s.union({4,5})) # Does the union operation on set s and the entered set i.e {4,5}
s= {4,5,6}  
print(s.intersection({4})) # Returns a new set with all the items common from two sets
print(s)
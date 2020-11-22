l1 = [1,3,4.5,2.11,98,34]

l1_sorted = l1.sort() # sorts the original list and doesn't return anything
print(l1_sorted) 
print(l1)

l1.reverse() # reverses the list
print(l1)

l1.append('A') # adds element at the end of the string
print(l1)

l1.insert(2,540)
print(l1)
l1.insert(20,1080) # If input index > size of list then value will be inserted at the end
print(l1)
l1.remove(4.5)
print(l1)
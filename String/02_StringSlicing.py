greeting = "Good Morning "

name = "AMANKumar"
#ind:   0(A)1(M)2(A)3(N)4(K)5(u)6(m)7(a)8(r)
#ind:   -9(A)-8(M)-7(A)-6(N)-5(K)-4(u)-3(m)-2(a)-1(r)

print(type(name))

# Concatenating two strings
c = greeting + name

print(c)
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# name[3] = 'd' --> doesn't work, Strings are mutable object(Check)


#String Slicing
# string[int start : int end] first index included and last index isn't included
print(name[1:5])
print(name[:5]) # is same as print(name[0:5])
print(name[2:]) # is same as print(name[2:LENGTH of String])

print(name[-1]) # prints the last character from string
print(name[-1:-4]) # will be null as start index is more than end index
print(name[-4:-1]) # Negative index assignment, i.e -1 is assigned to last letter

# Slicing with Skip value
# string[a:b:c], a is Start index (included) b is excluded end index and c is the skip lenght
d = name[0:6:1] # Skipping one character, as usual ther won't be any change
print(d)
e = name[0:6:2] # Skipping two character
print(e)
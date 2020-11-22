# The range function in python is used to generate a sequence of numbers.
# range (end) : goes from 0 to end-1
# range (start, end) : goes from start to end-1
# We can also specify the start, stop and step-size as follows
# range (start, stop, step-size)

for i in range(10):
    print(i)

else:
    print("For loop ended")

for j in range(2, 8):
    print(j)

print("NEW FOR LOOP")
for k in range(2, 8, 2):
    print(k)
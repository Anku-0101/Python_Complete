'''
The random access memory is volatile and all its contents are lost once a program terminates.
In order to persist the data foreever, files are used. 

A file is data stored in a storage device. A python program can talk to the file by reading content from it 
and writing content to it

RAM = Volatile
HDD = Non Volatile
'''
#   Types of files
#   1. Text files (.txt, .c etc)
#   2. Binary files (.jpg, .dat etc)

# Python has a lot of functions for reading, updating and deleting files.

# Python has an open() function for opening files. It takes 2 parameters : filename and mode.
# open("anyfile.txt", "r"), By default the mode is read(r)

f = open('sample.txt', 'r')
data = f.read() # data = f.read(5) -> reads only first 5 characters 
print(data)
f.close()


f_write = open('sample.txt', 'w')
f_write.write(" added from python code")
f_write.close()


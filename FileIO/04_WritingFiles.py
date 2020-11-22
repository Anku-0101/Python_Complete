'''
In order to write to a file, we first open it in write or append mode after wich, we use the 
python's f.write() method to write to the file 

'''

f = open('sample.txt','w')
f.write("Please write this to the file")
f.write("\n add this line too")
f.close()

# Everytime the code executes this will append the content at the end of append.txt
f_ = open('append.txt', 'a')
f_.write("  Add the contents")
f_.close()
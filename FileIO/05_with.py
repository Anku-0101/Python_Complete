'''
    With Statement 

The best way to open and close the file automatically is the with statement 

with open("this.txt") as f:
    f.read()  ## No need to write f.close() as it is done automaticlly  
'''
with open('another.txt', 'a') as f :
    f.write(" This text is appended ")

with open('another.txt', 'r') as f_:
    data = f_.read()
    print(data)
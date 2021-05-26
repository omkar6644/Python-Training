#open a file in read mode
with open('new.txt','r')as f:
    #reads complete data from the file
    data = f.read()
    #reads the specified number of bytes
   #data = f.read(15)
   #reads the first line of the file
    #data = f.readline()
    #reads all lines of the files and returns it as a list
    #data = f.readlines()

print(data)
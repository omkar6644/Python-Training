#open a image in read mode
with open('img.jpg','rb')as f:
    #read() reads entire content of the file
    data = f.read()
    print(data)
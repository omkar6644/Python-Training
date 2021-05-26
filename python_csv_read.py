#import csv module
import csv

#open a csv file in read mode
with open("emp.csv",'r')as f:
    #call reader method on file
    r = csv.reader(f)
    #convert to list
    data = list(r)
    print(data)
    print(type(data))
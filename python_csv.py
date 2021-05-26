#import csv module
import csv

#open a csv file in write mode
with open("emp.csv",'w')as f:
    #call writer() on file
    w = csv.writer(f)
    #using writerow add contents to the file
    w.writerow(["EID", "ENAME", "EAGE", "EDES"])
    w.writerow([101, "xyz", 18, 1000])
    w.writerow([102, "abc", 20, 2000])
    w.writerow([101, "qpr", 22, 3000])
f.close()
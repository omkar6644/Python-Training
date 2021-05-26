#open a file or create a new file in write mode
with open("employee.txt",'w')as e:
    Name = "xyz"
    Eid = "120"
    Phone_no = "88852"
    Place = "Karnataka"
    data = Name+ " " +Eid+ " " +Phone_no+ " " +Place
    #add data to the file
    e.write(data+"\n")
e.close()
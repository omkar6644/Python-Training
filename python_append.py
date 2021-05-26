#open a file in append mode so that no changes are made to the existing contents of the file
with open('employee.txt','a')as e:
    Designation = "Trainee"
    e.write(Designation)
e.close()
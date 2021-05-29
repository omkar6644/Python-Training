#import json
import json
class Student:
    #Student class constructor to initialize empty json string
    def __init__(self):
        self.json_str='{}'
    
    #method to insert data to the file
    def insertStudent(self):
        name= input("Enter the Name of Employee : ")
        lname = input("Enter the Last Name of Employee : ")
        id1 = int(input("Enter ID of Employee : "))
        age = int(input("Entr the age of Employee: "))
        stream = input("Enter the stream : ")
        salary = int(input("Enter the Salary "))
        
        f = open("Student.txt","r")
        self.json_str = f.readline()
        f.close()
        d = json.loads(self.json_str)
        data = {"name":name,"lname": lname,"id":id1, "age": age, "stream":stream, "salary": salary,}
        d["students"].append(data)
        
        
        self.json_str = json.dumps(d) 
        f = open("Student.txt","w")
        f.write(self.json_str)
        f.close()
        print("Inserted successfully")
        
    #method to display entire content of the file
    def selectAll(self):
        f=open("Student.txt","r") 
        data =f.read()
        f.close()
        dict = json.loads(data)
        print(dict)
        f.close()
        
        
    #method to update the existing content of the file    
    def update(self):
        id1 = int(input("Enter the ID of the student :"))
        f = open("Student.txt","rt") 
        self.json_str = f.readline()
        f.close()
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if i["id"] == id1:
                name = input("Enter name of student : ")
                id   = int(input("Enter the id : "))
                stream = input("Enter the stream of student : ")
                i["name"] = name
                i["id"] = id
                i["stream"] = stream
                d["students"] = data
                self.json_str = json.dumps(d)
            
       
                f= open("Student.txt","wt")
                f.write(self.json_str)
                f.close()
                print("Successfully updated")
                break
            
        else:
            print("Please enter a valid id")
        
      
    #method to delete particular element of the file    
    def delete(self):
        id1 = int(input("Enter the ID of the student : "))
        f = open("Student.txt","rt")
        self.json_str = f.readline()
        f.close()
        d = json.loads(self.json_str) 
        data = d["students"]
        c = 0
        for i in data:
            c = c+1
            if i["id"] == id1:
                del data[c-1]
                d["students"] = data
                self.json_str = json.dumps(d)
                f = open("Student.txt","wt")
                f.write(self.json_str)
                f.close() 
                print("Successfully deleted")
                break
        else:
            print("Enter a valid Id")

            
    #method to revtrive by specifying name        
    def selectSome(self):
        name = input("Enter the name of student : ")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if i["name"] == name:
                print(i)
                break
        else:
            print("Enter a valid name")
            
            
    #method to update contents depending upon the condition
    def updateOnCondition(self):
        id1 = int(input("Enter the ID of the student :"))
        stream = input("Enter the stream :" )
        f = open("Student.txt","rt") 
        self.json_str = f.readline()
        f.close()
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if (i["id"] < id1 and i["stream"] == stream):
                name = input("Enter Name of Student : ")
                id = int(input("Enter ID of Student : "))
                stream = input("Enter  stream of the Student : ")
                i["name"] = name
                i["id"] = id
                i["stream"] = stream
                d["students"] = data
                self.json_str = json.dumps(d)
            
       
                f= open("Student.txt","wt")
                f.write(self.json_str)
                f.close()
                print("Successfully updated")
                break
            
        else:
            print("Please enter a valid id or valid stream")
        
    
    #method to update only name of the student
    def updateName(self):
        id1 = int(input("Enter the ID of the student :"))
        f = open("Student.txt","rt") 
        self.json_str = f.readline()
        f.close()
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if i["id"] == id1:
                name = input("enter name :")
                i["name"] = name
                d["students"] = data
                self.json_str = json.dumps(d)
            
       
                f= open("Student.txt","wt")
                f.write(self.json_str)
                f.close()
                print("Successfully updated")
                break
            
        else:
            print("Please enter a valid id")
            
    
    
    #method to update only stream of the student
    def updateStream(self):
        id1 = int(input("Enter the ID of the student :"))
        f = open("Student.txt","rt") 
        self.json_str = f.readline()
        f.close()
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if i["id"] == id1:
                stream = input("Enter stream :")
                i["stream"] = stream
                d["students"] = data
                self.json_str = json.dumps(d)
            
       
                f= open("Student.txt","wt")
                f.write(self.json_str)
                f.close()
                print("Successfully updated")
                break
            
        else:
            print("Please enter a valid id")
            
    
    #method to select only name of employee
    def select(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            print(i["name"].upper())
            
     
    #method to count number of employees
    def selectCount(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        c =0
        for i in data:
            c=c+1
        print("The number of Employees are :", c)
        
        
    
    #method to fetch salary of a particular employee
    def selectS(self):
        name = input("Enter the name of employee to fetch their salary : ")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if i["name"] == name:
                print("The salary of employee is :",i["salary"])
                break
        else:
            print("Enter a valid name")
            
    
    #method to get details of employee based on the salary
    def selectDetails(self):
        salary = input("Enter the range of salary : ")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if i["salary"] < salary :
                print(i)
                
    
    #method to delete last emplyees data
    def pop(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        data.pop()
        
        d["students"]=data
        self.json_str = json.dumps(d)
        f= open("Student.txt","wt")
        f.write(self.json_str)
        f.close()
        print("Successfully updated")
        
        
    #method to get maximum age of employee
    def maxAge(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a =[]
        for i in data:
            if i["age"]>=0:
                a.append(i["age"])
        return max(a)
    
    
    
    #method to get minimum age of employee
    def minAge(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a =[]
        for i in data:
            if i["age"]>=0:
                a.append(i["age"])
        return min(a)
    
    
    #method to get minimum salary of employee
    def minSalary(self):
        #salary = input("Enter the range of salary : ")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a =[]
        for i in data:
            if i["salary"] >= 0:
                a.append(i["salary"])
        return min(a)
    
    
    #method to get maximum salary of employee
    def maxSalary(self):
        #salary = input("Enter the range of salary : ")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a =[]
        for i in data:
            if i["salary"] >= 0:
                a.append(i["salary"])
        return max(a)
           
    
    
    #method to get sum of salary employee
    def sumOfSalary(self):
        #salary = input("Enter the range of salary : ")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a =[]
        for i in data:
            if i["salary"] >= 0:
                a.append(i["salary"])
        return sum(a)
    
    
    #method to fetch name of employee by specifying starting letter
    def nameStartsWith(self):
        start = input("Enter the starting letter :")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a =[]
        for i in data:
            if i["name"]:
                a.append(i["name"])
            if a:
                letter = [x for x in a if x.startswith(start)]
        return letter
    
    """
    def nameEndsWith(self):
        end = input("Enter the ending letter :")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a =[]
        for i in data:
            if i["name"]:
                a.append(i["name"])
            if a:
                end = [x for x in a if x.endswith(end)]
        return end"""
    
    
    
    #method to clear data of all employees
    def clearAll(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        data.clear()
        print("Cleared successfully")
        
    
    #method to get header value
    def getHeaderValue(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a = []
        for i in data:
            for j in i:
                a.append(j)
            return a
        
    
    #method to display data orderly
    def getOrderedData(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            print(i)
     
    #method to get names of all employee
    def getNames(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a = []
        for i in data:
            if i["name"]:
                a.append(i["name"])
        return a
            
     
    #method to get names and age of all employee    
    def getNameAndAge(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a = []
        b = []
        for i in data:
            if i["name"]:
                a.append(i["name"])
        for j in data:
            if j["age"]:
                b.append(j["age"])
        return (list(zip(a,b)))
    
    #method to check whehter a name of employee is present 
    def CheckName(self):
        name = input("Enter the name to check whether it is present :")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        for i in data:
            if i["name"] == name:
                print("Name present")
                break
        else:
            print("Name not present")
            
    
    #method to reverse data of all employees
    def reverseData(self):
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        return (list(reversed(d["students"])))
    
    #method to get column data     
    def getColumnData(self):
        col = input("Enter the column name :")
        f = open("Student.txt", 'r')
        self.json_str = f.readline()
        f.close()
        
        d = json.loads(self.json_str)
        data = d["students"]
        a = []
        for i in data:
            if i[col]:
                a.append(i[col])
        return a
    
        
    
                
        

s = Student()
#s.select()
#s.selectCount()
#s.selectS()
#s.selectDetails()
#s.selectDetailOfMaxSalary()
#s.pop()
#s.insertStudent()
s.selectAll()
#print("The maximum age of employee is :",s.maxAge())
#print("The minimum age of employee is :",s.minAge())
#print("The minimum salary of employee is :",s.minSalary())
#print("The maximum salary of employee is :",s.maxSalary())
#print("The sum salary of employee is :",s.sumOfSalary())
#print(s.nameStartsWith())
#print(s.nameEndsWith())
#print(s.getHeaderValue())
#print(s.getOrderedData())
#print(s.getNames())
#print(s.getNameAndAge())
#s.CheckName()
#print(s.reverseData())
#print(s.getColumnData())
#s.delete()
#s.update()
#s.selectSome()
#s.updateOnCondition()
#s.updateName()
#s.updateStream()
#s.clear()
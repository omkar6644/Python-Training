#import Oracle module
import cx_Oracle

class Database:
    #constructor to establish connection and initialize cursor object
    def __init__(self):
        #establish a connection between program and the oracle database
        self.conn = cx_Oracle.connect("Om/omkar@localhost")

        #create a cursor object to execute a SQL query
        self.cursor = self.conn.cursor()
        
        
    #method to create a table with name employee
    def create(self):
        self.cursor.execute("create table employee(Eid int primary key, Ename varchar2(30), Elname varchar2(30), Eage int, Estream varchar2(20), Esalary float)")
        print("Table Created successfully")


        
    #method to insert data into the employee table
    def insert(self):
        id1 = int(input("Enter id :"))
        name = input("enter name :")
        lname = input("enter lname :")
        age = int(input("enter age :"))
        stream = input("enter stream :")
        salary = int(input("enter salary :"))
        sql = ('INSERT INTO employee(Eid, Ename, Elname, Eage, Estream, Esalary)' 'values(:id1, :name, :lname, :age, :stream, :salary)')
        val =(id1, name, lname, age, stream, salary)
        self.cursor.execute(sql,val)
        #commit() is used to perform the above operation
        self.conn.commit()
        print("records inserted successfully")
        #close the operation
        #cursor.close()
        #close the connection
        #conn.close()    
    
    def select(self):
        self.cursor.execute("SELECT * FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #self.cursor.close()
            #self.conn.close()
            
            
            
    #method to update data in the employee table
    def update(self):
        id1 = int(input("Enter the id to update : "))
        name = input("Enter new name :" )
        sql = ('UPDATE employee SET Ename = :name WHERE Eid = :id1')
        val = (name, id1)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("records updated successfully")
        #cursor.close()
        #conn.close()
        
        
    
    #method to delete data from the employee table
    def delete(self):
        id1 = int(input("Enter the id to delete :"))
        sql = ('DELETE from employee WHERE Eid = :id1')
        self.cursor.execute(sql, [id1])
        self.conn.commit()
        print("record deleted successfully")
        #cursor.close()
        #conn.close()

            
            
    #method to only display name and age of employee
    def selectNameAndAge(self):
        id1 = int(input("Enter the id :"))
        sql = ("SELECT Ename, Eage FROM employee WHERE Eid = :id1")
        self.cursor.execute(sql, [id1])
        res = self.cursor.fetchall()
        for x in res:
            print(x)
    #cursor.close()
    #conn.close()
    
    
    #method to select distinct streams
    def selectDistinctStream(self):
        self.cursor.execute("SELECT DISTINCT Estream FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()
            
            
    #method to count number of employees
    def countEmployees(self):
        self.cursor.execute("SELECT COUNT(*) FROM employee")
        res = self.cursor.fetchall()
        print(res)
        #cursor.close()
        #conn.close()
        
        
    
    #method to count number of characters in Ename
    def countCharacters(self):
        self.cursor.execute("SELECT LENGTH(trim(Ename))FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()



    #method to display Ename in Uppercase
    def nameUpperCase(self):
        self.cursor.execute("SELECT UPPER(Ename) FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()




    #method to display Ename in Lowercase
    def nameLowerCase(self):
        self.cursor.execute("SELECT LOWER(Ename) FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()




    #method to select Ename using As Clause
    def nameUsingAs(self):
        self.cursor.execute("SELECT Ename AS Workername FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()



    #method to select Distinct Elname of employee
    def selectDistinctLname(self):
        self.cursor.execute("SELECT DISTINCT Elname FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()



    #method to display position of particular character
    def positionOfCharacter(self):
        name = input("enter name :")
        sql = ("SELECT INSTR(ENAME, 'a') FROM employee WHERE Ename = :name")
        self.cursor.execute(sql, [ name])
        res = self.cursor.fetchall()
        print(res)
        #cursor.close()
        #conn.close()


    #method to select distinct Elname along with length
    def selectDistinctLength(self):
        self.cursor.execute("SELECT DISTINCT Elname, length(Elname) FROM employee")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()


    #method to display employee details who don't belong to the specified stream
    def selectOnCondition(self):
        stream = input("enter the stream :")
        sql = ("SELECT Eid, Ename FROM employee WHERE Estream NOT IN(:stream)")
        self.cursor.execute(sql, [stream])
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()


    #method to select maximum salary from employee table
    def selectMaxSalary(self):
        self.cursor.execute("SELECT MAX(Esalary) FROM employee")
        res = self.cursor.fetchall()
        print(res)
        #cursor.close()
        #conn.close()


    #method to select minimum salary from employee table
    def selectMinSalary(self):
        self.cursor.execute("SELECT MIN(Esalary) FROM employee")
        res = self.cursor.fetchall()
        print(res)
        #cursor.close()
        #conn.close()  


    #method to select Sum of salary from employee table
    def selectSumOfSalary(self):
        self.cursor.execute("SELECT SUM(Esalary) FROM employee")
        res = self.cursor.fetchall()
        print(res)
        #cursor.close()
        #conn.close()



    #method to select Average salary from employee table
    def selectAvgOfSalary(self):
        self.cursor.execute("SELECT AVG(Esalary) FROM employee")
        res = self.cursor.fetchall()
        print(res)
        #cursor.close()
        #conn.close()


    #method to select details of employee whose name start with 'O'
    def selectNameStartsWith(self):
        self.cursor.execute("SELECT * FROM employee WHERE Ename LIKE 'O%'")
        res = self.cursor.fetchall()
        print(res)
        #cursor.close()
        #conn.close()


    #method to select Ename in alpahbetical order
    def selectNameAlphabetically(self):
        self.cursor.execute("SELECT Ename FROM employee ORDER BY Ename")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()



    #method to select Ename in descing order
    def selectNameDescOrder(self):
        self.cursor.execute("SELECT Ename FROM employee ORDER BY Ename DESC")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()


    #method to select employee details using having clause
    def selectUsingHavingClause(self):
        self.cursor.execute("SELECT COUNT(Eid), Ename FROM employee GROUP BY Ename having COUNT(Eid) <4")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            #cursor.close()
            #conn.close()
            
            
    #method to select details of employee whose salary is greater than the specified salary      
    def selectOnSalary(self):
        sal = int(input("Enter the salary :" ))
        sql = ("SELECT * FROM employee WHERE Esalary > :sal")
        self.cursor.execute(sql, [sal])
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            
    
    #method to select details of employee whose salary is less than the specified salary       
    def selectSalaryOnCondition(self):
        sal = int(input("Enter the salary :" ))
        sql = ("SELECT * FROM employee WHERE Esalary < :sal")
        self.cursor.execute(sql, [sal])
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            
   
    #method to select details of employee using in keyword        
    def selectDetailsUsingIn(self):
        self.cursor.execute("SELECT * FROM employee WHERE Estream IN('Big Data','NS')")
        res = self.cursor.fetchall()
        for x in res:
            print(x)
            
    
    #method to select details of employee within a specific range of salary
    def selectDetailsWithinRange(self):
        self.cursor.execute('SELECT * FROM employee WHERE Esalary BETWEEN 20000 AND 26000')
        res = self.cursor.fetchall()
        for x in res:
            print(x)
        
    
d = Database()
#d.select()
#d.create()
#d.insert()
#d.update()
#d.delete()
d.selectNameAndAge()
#d.selectDistinctStream()
#d.countEmployees()
#d.countCharacters()
#d.nameUpperCase()
#d.nameLowerCase()
#d.nameUsingAs()
#d.selectDistinctLname()
#d.positionOfCharacter()
#d.selectDistinctLength()
#d.selectOnCondition()
#d.selectMaxSalary()
#d.selectMinSalary()
#d.selectSumOfSalary()
#d.selectAvgOfSalary()
#d.selectNameStartsWith()
#d.selectNameAlphabetically()
#d.selectNameDescOrder()
#d.selectUsingHavingClause()
#d.selectOnSalary()
#d.selectSalaryOnCondition()
#d.selectDetailsUsingIn()
#d.selectDetailsWithinRange()
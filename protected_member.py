class Employee:
     def __init__(self, id , name , designation):  
            #protected data members
          self._id = id 
          self._name = name
          self._designation = designation

       #protected function
     def _display(self):
          print(self._id)
          print(self._designation)
  
class Employee2(Employee):
       def __init__(self, id , name , designation): 
                Employee.__init__(self, id , name , designation) 
          
       def displayDetails(self):
                print(self._name) 
                self._display()#protected data members can be accessed by the derived class
        
e = Employee2(15444,"xyz","software developer" ) 
e.displayDetails() 
#e._diplay() #protected data members cannot be accessed outside the class

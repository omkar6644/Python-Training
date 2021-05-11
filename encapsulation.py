#encapsulation of private methods
#encapsulation is a process of binding the data and code together or it is the process of providing controlled access to the private members of the class.
class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
#redcar.__updateSoftware()
print()
print()

#encapsulation of private variables
class Book:
    def __init__(self,name):
        self.__name=name
    def setName(self,values):
        self.__name=values
    def getName(self):
        return self.__name
b=Book("think rich")
#print(b.name) cannot acess private variables of class 
b.setName("grow rich") #by using setname method we can access private variables 
x=b.getName()
print(x)
print()
print()


#using Property() function to provide a common name to setter and getter method
class Student:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
    getSet=property(getter,setter)
s=Student()
s.getSet="Python"
msg=s.getSet
print(msg)
print()
print()

#using @Property Decorator
#@property decorator is used to common name to the setter and getter method
class Student:
    def __init__(self):
        self.__name=""
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
s=Student()
s.name="Java"
msg=s.name
print(msg)

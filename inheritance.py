#inheritance in python
#inheritance is a process of reusing the existing code, adding on properties and behaviour to the derived class.
#single inheritance
#in single inheritance there is one parent class and one child class
class Plane:
    def takeOff(self):
        print("plane took off")
    def fly(self):
        print("plane is flying")
class Cargo(Plane):
    def cargoPlane(self):
        print("cargo plane")
    def land(self):
        print("plane is landing")
c=Cargo()
c.cargoPlane()
c.takeOff()
c.fly()
c.land()
print()
print()
#multi-level inheritance
#in multi-level inheritance, here A is the parent of B and likewise B is the parent class C, so class C inherits methods from class A as well as class B. 
class Plane:
    def takeOff(self):
        print("plane took off")
    def fly(self):
        print("plane is flying")
class Cargo(Plane):
    def cargoPlane(self):
        print("cargo plane")
    def land(self):
        print("plane is landing")
class PassengerPlane(Cargo):
    def Passenger(self):
        print("passenger plane")
c=Cargo()
c.cargoPlane()
c.takeOff()
c.fly()
c.land()
print()
p=PassengerPlane()
p.Passenger()
p.takeOff()
p.fly()
p.land()
print()
print()
#hierarchial inheritance
#in hierarchial inheritance Class A is a parent to two classes B and C.
class Plane:
    def takeOff(self):
        print("plane took off")
    def fly(self):
        print("plane is flying")
    def land(self):
        print("plane is landing")
class Helicopter(Plane):
    def heli(self):
        print("Helicopter")
class FighterPlane(Plane):
    def figh(self):
        print("Fighter plane")
h=Helicopter()
h.heli()
h.takeOff()
h.fly()
h.land()
print()
f=FighterPlane()
f.figh()
f.takeOff()
f.fly()
f.land()
print()
print()

#Multiple inheritance
#in multiple inheritance child class C has two parent classes i.e A and B.
class Plane:
    def takeOff(self):
        print("plane took off")
    def fly(self):
        print("plane is flying")
    
class Helicopter:
    def land(self):
        print("plane is landing")
class Jets(Plane,Helicopter):
    def jet(self):
        print("Jet plane")
j=Jets()
j.jet()
j.takeOff()
j.fly()
j.land()
print()
print()

#cyclic inheritance is not supported in python because of infinite loop.

#overidden methods in inheritance
#the process of redefining a method that is already defined in the parent by the child is refered as overidding.
class Animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
class Tiger(Animal):
    def eat(self): #overidden method
        print("tiger hunts and eats")
class Deer(Animal):
    def eat(self):#overidden method
        print("deer will graze and eat")
t=Tiger()
t.eat()
t.sleep()
d=Deer()
d.eat()
d.sleep()
print()
print()

#inheritance using __init__()
class Employee:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def display(self):
    print(self.firstname, self.lastname)

class Employee2(Employee):
  def __init__(self, fname, lname):
    Employee.__init__(self, fname, lname) #we have to explicitly call parent class constructor in child class

e = Employee2("Omkar", "Patil")
e.display()
print()
print()
#inheritance using super() method
class Employee:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def display(self):
    print(self.firstname, self.lastname)

class Employee2(Employee):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) #super method inherits all the methods from the parent class and we have to explicitly call it without passing self as parameter.

e = Employee2("Omkar", "Patil")
e.display()
print()
print()

#adding properties to child class

class Employee:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def display(self):
    print(self.firstname, self.lastname)

class Employee2(Employee):
  def __init__(self, fname, lname,year): #add property as parameter to child class constructor
    super().__init__(fname, lname)
    self.year=year
e = Employee2("Omkar", "Patil",2021)
e.display()
print(e.year) #displaying the property added to child class
print()
print()

#super() without parameters
class Vehicle:
    def __init__(self):
        self.btyre = 2
        self.bsports = True
        self.ctyre=4
        self.csports=True
    def isBike(self):
        if self.btyre==2:
            print("It is a bike")
     
    def isSports(self):
        if self.bsports:
            print("It is a sports bike")
    def isCar(self):
        if self.ctyre==4:
            print("it is a car")
    def isSportsCar(self):
        if self.csports:
            print("it is a sports car")
            
     
class Bike(Vehicle):
    def __init__(self):
        super().__init__() #without parameters
 
class Car(Vehicle):
    def __init__(self):
        super().__init__() #without parameters
b= Bike()
b.isBike()
b.isSports()
c=Car()
c.isCar()
c.isSportsCar()

#import ABC class from abc module
from abc import ABC   
class Car(ABC):
    #abstract method
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")

        
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")
        
        
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")
          
   
          
   
t= Tesla ()   
t.mileage()     
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  

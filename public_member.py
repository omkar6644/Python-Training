class Parent:
     def __init__(self):
        # public data mambers 
           self.a = 10
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b = 20
c = Child()
print(c.a) #public member can accessed anywhere throughout the program
print(c.b)

#parent class
class Parent:
    def __init__(self):
        self.__a = 10
    def __display():
        print(self.__a)

#child class
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
    def fun(self):
        self.__display()
c = Child()
c.fun()

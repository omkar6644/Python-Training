#the below program takes 3 inputs from the user and finds a quadratic equation.
#import square root function from math module
from math import sqrt
a = float(input("a=: "))
b = float(input("b=: "))
c = float(input("c=: "))

#Quadratic function 
def quadEqu(a, b ,c):
    d = b**2-4*a*c
    if d > 0:
        x = (((-b)+sqrt(d))/(2*a))     
        y = (((-b)-sqrt(d))/(2*a))
        return x,y
        if x or y == 0:
            return 
        else:
            return 1
print(quadEqu(a,b,c))

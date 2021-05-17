class Stack:
    def __init__(self):
        self.s=[]
 
#add the elements to stack
    def addElement(self,data):
        self.s=self.s+[data]
#popping elements from stack
    def pop(self):
        if self.s==[]:
            return "stack is empty"
        else:
            ele=self.s[len(self.s)-1]
            del self.s[len(self.s)-1]
            return ele
#Display the elements of stack
    def display(self):
        print(self.s)
s1=Stack()
s1.addElement(1)
s1.addElement(2)
s1.addElement(3)
print("Stack after inserting elements")
s1.display()
s1.pop()
print("Stack after poping:")
s1.display()



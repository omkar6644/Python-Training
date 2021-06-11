class Node:
    # node class constructor to initializes data and next
    def __init__(self, value):
        self.value = value
        self.next = None
     
class Stack:
     
    # head is set to None
    def __init__(self):
        self.head = None
     
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    
    # adds element to stack
    def push(self,data):
         
        if self.head == None:
            self.head=Node(data)
             
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
     
    # Remove element from the stack
    def pop(self):
         
        if self.isempty():
            return None    
        else:
            n = self.head
            self.head = self.head.next
     
    # Prints the stack    
    def display(self):
        n=self.head
        while n is not None:
            print(n.value)
            n=n.next
        
    
         

s = Stack()
s.push(11)
s.push(22)
s.push(33)
s.push(44)
s.display()
print()
s.pop()
s.display()

 
 

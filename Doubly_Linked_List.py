class Node:
    #Node class constructor to initialize data, next, prev
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
 

class DoublyLinkedList:
    #Linkedlist class constructor to initialize head
    def __init__(self):
        self.head = None

    #adding elements to the list

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    #adding element at beginning of list
    def addAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    #deleting node from list
    def deleteNode(self, x):
        if self.head is None:
            return
        if self.head == x:
            self.head = x.next
        if x.next is not None:
            x.next.prev=x.prev
        if x.prev is not None:
            x.prev.next=x.next
    
    #adding element at end of list
    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    #getting node after specified value
    def getNodeAfterValue(self,data):
        val = self.head      
        while val:  
            if val.value==data: 
                val = val.next  
                res1=val.value  
                break
            val = val.next
        return res1

    #getting node before specified value
    def getNodeBefore(self,data):
        n=self.head
        while n is not None:
            if n.value==data:
                res=n.prev
                res1=res.value
            n=n.next
        return res1

    #reversing the list
    def reverseLinkedlist(self):
        prev = None
        while self.head: 
            next = self.head.next 
            self.head.next = prev  
            prev = self.head        
            self.head = next        
        self.head = prev

    #counting the number of elements in the list
    def count(self):
        temp=self.head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        return count
     #printing elements of the list
    def printList(self):
        if self.head is None:
            return
        else:
            n=self.head
            while n is not None:
                print(n.value)
                n=n.next
        
 
d = DoublyLinkedList()
d.add(10)
d.add(20)
print("adding at beginning")
d.addAtBegin(1)
d.addAtBegin(2)
d.addAtBegin(3)
d.printList()
print()
print("after deleting")
d.deleteNode(d.head.next)
d.printList()
print()
print()
print("adding at end")
d.addAtEnd(1000)
d.printList()
print()
print()
print(d.getNodeAfterValue(1))
print()
print()
print(d.getNodeBefore(1))
print()
d.reverseLinkedlist()
d.printList()
print()
print()
print("No of elements in list is: ",d.count())

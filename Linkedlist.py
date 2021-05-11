# Linked list operations in Python


# Create a node
class Node:
    #Node constructor
    def __init__(self,value):
        self.value = value
        self.next = None

#Create LinkedList
class LinkedList:
    #Linkedlist constructor
    def __init__(self):
        self.head = None

    # Adding  at the beginning
    def addAtBeginning(self, data):
        new_node = Node(data) #object of Node class
        new_node.next = self.head  #change next of new node to point head
        self.head = new_node #change head to recently added node

    # Adding at particular node
    def addAtNode(self, node, data): #node is passed as head of the list
        if node is None: #if the node is not present return None
            return

        new_node = Node(data)
        new_node.next = node.next #assign new_node_next with head.next value
        node.next = new_node    #assign head.next value as newly created value

     # Adding at the end
    def addAtEnd(self, data):
        new_node = Node(data) 
        last_node = self.head  #assing last node as head
        while (last_node.next): #traverse until we reach  last node
            last_node = last_node.next      #get the value of last node
        last_node.next = new_node  #change next of last node to newly created node
    #Deleting nodes
    def deleteNode(self, x):
        if self.head is None: #check if head is None if none return none
            return
        n = self.head #assign n as head
        while n.next is not None: #Traverse to element to be deleted
            if n.next.value == x: #check if the value of the node being iterated is equal to the value to be deleted
                break
            n = n.next # set reference of the previous node to the node which exists

        if n.next is None:
            return 
        else:
            n.next = n.next.next 
    #Reversing a Linkedlist
    def reverseLinkedlist(self):
        prev = None
        while self.head is not None: 
            next = self.head.next #assign head to next
            self.head.next = prev  #set value of the current node to prev
            prev = self.head        #set prev to current node
            self.head = next        #set current to value of next
        self.head = prev            #at the end of loop prev will point to last node so set it as head


    #Counting number of nodes in a linkedlist
    def count(self):
        if self.head is None: #if head is none, implies list is empty
            return 
        n = self.head  #n variable is assigned with head value
        count = 0       #count is initialize to 0
        while n is not None:  #iterate until n is none
            count = count + 1  #increment count for each head value
            n = n.next          #assign n with next head value
        return count            #returns the count of elements

     #Printing nodes of the Linkedlist
    def printList(self):
        current_node = self.head  #assign current_node with head value
        while (current_node):       #iterate until cureent_node is not none
            print(current_node.value)   #prints value of the current node
            current_node = current_node.next  #reassing current_node with next node

#Main function
if __name__ == '__main__':
    llist = LinkedList()
    llist.addAtBeginning(1)
    llist.addAtBeginning(2)
    llist.addAtBeginning(3)
    print("Linkedlist after inserting elements at beginning")
    llist.printList()
    print()
    print()
    print("Linkedlist after inserting elements at the end")
    llist.addAtEnd(9)
    llist.printList()
    print()
    print()
    llist.addAtNode(llist.head, 5)
    print("Linkedlist after inserting elements at a specified position")
    llist.printList()
    print()
    print()
    llist.deleteNode(2)
    print("Linkedlist after deleting specific value")
    llist.printList()
    print()
    print()
    llist.reverseLinkedlist()
    print("Reversed Linkedlist")
    llist.printList()
    print()
    print()
    print("Length of the linkedlist is: ",llist.count())
      
    
    

class Node:
	#node class constructor to initialize value and next.
    def __init__(self, value):
       self.value = value
       self.next = None
 
class Queue:
	#Queue class constructor to initialize head and last.
    def __init__(self):
        self.head = None
        self.last = None
 
	#method to add elements to the queue
    def add(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

 	#mehtod to pop elements out of queue
    def pop(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.value
            self.head = self.head.next
            return to_return

	#method to display elements of quueu
    def display(self):
        if self.head is None:
            return
        else:
            n=self.head
            while n is not None:
                print(n.value)
                n=n.next
 
q = Queue()
q.add(1)
q.add(2)
q.display()
q.pop()
print()
q.display()

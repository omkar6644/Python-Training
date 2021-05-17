class Queue:
    def __init__(self):
        self.queue=[]
#add the elements to queue
    def addElement(self,data):
        self.queue=self.queue+[data]
#poping elements from queue
    def pop(self):
        if self.queue==[]:
            print("queue is empty")
        else:
            ele=self.queue[0]
            del self.queue[0]
            return ele
#Display the elements of queue
    def display(self):
        return self.queue
q=Queue()
q.addElement(1)
q.addElement(2)
q.addElement(3)
print("Queue after inserting elements",q.display())
q.pop()
print("Queue after poping:")
print(q.display())



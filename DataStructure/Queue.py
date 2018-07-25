'''
 Purpose: Implementing a  Queue for Banking operation
 @author Nikhil Patil

 '''
class Queue:

    def __init__(self,size,people):
        self.size = size
        self.rear = people
        self.front = 0
        self.arr = []
        print "Queue is ready :"

    def Enque(self):
        if (self.isFull()):
            print "Queue is full"
        else:
            self.rear = self.rear + 1

    def Deque(self):
        if (self.isEmpty()):
            print "Queue is empty"
        else:
            self.front =self.front + 1

    def isFull(self):
        return (self.rear == self.size)

    def isEmpty(self):
        return (self.front == self.rear)

    def NumOfPeople(self):
        return (self.rear - self.front)

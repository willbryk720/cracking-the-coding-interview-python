'''
Design a class MyQueue that implements a queue using two stacks
'''

from Stack import Stack

class MyQueue():
    def __init__(self):
        self.data_stack = Stack()
        self.helper_stack = Stack()

    def enqueue(self, value):
        self.data_stack.push(value)

    def isEmpty(self):
        return self.data_stack.isEmpty()

    def dequeue(self):
        stack_size = self.data_stack.size()
        for i in range(stack_size - 1):
            top = self.data_stack.pop()
            self.helper_stack.push(top)
        val = self.data_stack.pop()
        for i in range(stack_size - 1):
            top = self.helper_stack.pop()
            self.data_stack.push(top)
        return val

    def size(self):
        return self.data_stack.size()
    
    def printQueue(self):
        self.data_stack.printStack()

Q = MyQueue()

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
Q.enqueue(6)

Q.printQueue()
print "Val:", Q.dequeue()
Q.printQueue()
print "Val:", Q.dequeue()
Q.printQueue()
Q.enqueue(7)
print "Val:", Q.dequeue()
Q.printQueue()
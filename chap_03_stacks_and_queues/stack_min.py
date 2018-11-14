'''
Design stack such that it has a function min that returns the minimum element
'''

from Stack import Stack

class StackWithMin(Stack):
    def __init__(self):
        Stack.__init__(self)
    
    def push(self, value):
        top = self.peek()
        if top == None:
            self.items.append((value, value))
        else:
            self.items.append((value, min(top[1], value)))
    
    def pop(self):
        return super(StackWithMin, self).pop()[0]
    
    def getMin(self):
        return self.peek()[1] if self.peek() != None else None

S = StackWithMin()

S.push(5)
S.push(3)
S.push(8)
S.push(2)
print S.getMin()
print S.pop()
print S.getMin()
print S.pop()
S.printStack()
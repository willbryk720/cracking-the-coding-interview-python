'''
Design stack SetOfStacks that creates a new stack under the hood when the size exceeds a threshold
Should operate like a normal stack
'''

from Stack import Stack

class SetOfStacks():
    def __init__(self, threshold):
        self.stacks = [Stack()]
        self.threshold = threshold
    
    def curStack(self):
        return self.stacks[-1]
    
    def push(self, value):
        curStack = self.curStack()
        if curStack.size() == self.threshold:
            self.stacks.append(Stack())
            self.curStack().push(value)
        else:
            curStack.push(value)
    
    def pop(self):
        curStack = self.curStack()
        val = curStack.pop()

        if self.curStack().size() == 0 and len(self.stacks) > 1:
            del self.stacks[-1]

        return val
        
    def printStack(self):
        for i, stack in enumerate(self.stacks):
            print "Stack-" + str(i)
            stack.printStack()
            
    def isEmpty(self):
        return len(self.stacks) == 1 and self.curStack().size() == 0

    def peek(self):
        if self.isEmpty:
            return None
        else:
            return self.curStack().peek()

    def size(self):
        return sum([stack.size() for stack in self.stacks])

S = SetOfStacks(3)

S.push(5)
S.push(3)
S.push(8)
S.push(2)
S.push(7)
S.push(5)
S.push(4)

S.printStack()
print S.size()
print "------"
for i in range(10):
    print S.pop()
S.printStack()
S.push(4)
S.printStack()




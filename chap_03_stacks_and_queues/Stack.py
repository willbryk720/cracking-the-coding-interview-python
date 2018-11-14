class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if len(self.items) == 0:
            return None
        val = self.items[-1]
        del self.items[-1]
        return val
        
    def printStack(self):
        print self.items

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)


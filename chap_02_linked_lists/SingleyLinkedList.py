class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertNodeAtEnd(self, value):
        curNode = self.head
        newNode = Node(value)

        if curNode == None:
            self.head = newNode
            return 
        
        while curNode.next != None:
            curNode = curNode.next
        
        curNode.next = newNode
    
    def insertNodeAtBeginning(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    
    def getList(self):
        '''
        Returns linked list as a list
        '''
        curNode = self.head
        lst = []
        while curNode is not None:
            lst.append(curNode.value)
            curNode = curNode.next
            
        return lst
    
            
            




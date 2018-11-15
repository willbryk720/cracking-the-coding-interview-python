class Node:
    def __init__(self, value = None):
        self.value = value
        self.children = []
        


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def addLeft(self, tree):
        self.left = tree
    
    def addRight(self, tree):
        self.right = tree
    
    def printTree(self):
        print "root: ", self.value
        self.recPrintTree(self, self)
    
    def recPrintTree(self, tree, parent = None, isLeft = None):
        if tree == None:
            return
        else:
            # print info
            if parent != None:              
                print tree.value, "left of " if isLeft else "right of ", parent

            self.recPrintTree(tree.left, tree.value, True)
            self.recPrintTree(tree.right, tree.value, False)
    
    def breadthFirstPrint(self):
        queue = [self]

        while len(queue) > 0:
            for i in range(len(queue)):
                subTree = queue.pop()
                print subTree.value

                if subTree.left != None:
                    queue.insert(0, subTree.left)
                if subTree.right != None:
                    queue.insert(0, subTree.right)
            print "----"
    
    def depthFirstPrint(self, tree):
        if tree == None:
            return

        self.depthFirstPrint(tree.left)
        self.depthFirstPrint(tree.right)
        print tree.value


# B = BinaryTree(5)
# lB = BinaryTree(4)
# llB = BinaryTree(3)
# rlB = BinaryTree(4.5)
# rB = BinaryTree(7)
# rrB = BinaryTree(9)
# '''
#                 5
#         4               7
#     3       4.5             9
# '''

# lB.addLeft(llB)
# lB.addRight(rlB)
# rB.addRight(rrB)
# B.addLeft(lB)
# B.addRight(rB)
# B.breadthFirstPrint()
# B.depthFirstPrint(B)

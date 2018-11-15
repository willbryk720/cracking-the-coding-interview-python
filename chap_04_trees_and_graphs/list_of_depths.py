'''
Design an algorithm that creates a list for the nodes at each depth
'''

from Tree import BinaryTree

def list_of_depths(tree):
    queue = [tree]

    while len(queue) > 0:
        linked_lst = []
        for i in range(len(queue)):
            subTree = queue.pop()
            linked_lst.append(subTree.value)

            if subTree.left != None:
                queue.insert(0, subTree.left)
            if subTree.right != None:
                queue.insert(0, subTree.right)
        print linked_lst
        print "----"
    

B = BinaryTree(5)
lB = BinaryTree(4)
llB = BinaryTree(3)
rlB = BinaryTree(4.5)
rB = BinaryTree(7)
rrB = BinaryTree(9)
'''
                5
        4               7
    3       4.5             9
'''

lB.addLeft(llB)
lB.addRight(rlB)
rB.addRight(rrB)
B.addLeft(lB)
B.addRight(rB)

list_of_depths(B)
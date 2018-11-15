'''
Write function that checks if a tree is balanced
'''

from Tree import BinaryTree

def check_balanced(tree):
    print (tree.value if tree != None else None )
    
    if tree == None:
        print 0
        return 0
    
    left_depth = check_balanced(tree.left)
    right_depth = check_balanced(tree.right)

    # Bad if some subtree is bad
    if left_depth == -1 or right_depth == -1:
        return -1

    # Bad if depths are different by more than 1
    if abs(right_depth - left_depth) > 1:
        print "diff"
        return -1

    return max(right_depth, left_depth) + 1
        
        
B = BinaryTree(5)
lB = BinaryTree(4)
llB = BinaryTree(3)
rlB = BinaryTree(4.5)
rB = BinaryTree(7)
rrB = BinaryTree(9)
rrrB = BinaryTree(10)
'''
                5
        4               7
    3       4.5             9
'''

lB.addLeft(llB)
lB.addRight(rlB)
rB.addRight(rrB)
rrB.addRight(rrrB)
B.addLeft(lB)
B.addRight(rB)

print check_balanced(B)

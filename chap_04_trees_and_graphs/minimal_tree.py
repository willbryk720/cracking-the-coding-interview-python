from Tree import BinaryTree

def minimal_tree(arr):
    med = len(arr)/2

    left_arr = arr[:med]
    right_arr = arr[med+1:]

    val = arr[med]

    B = BinaryTree(val)

    if len(left_arr) > 0:
        B.addLeft(minimal_tree(left_arr))
    
    if len(right_arr) > 0:
        B.addRight(minimal_tree(right_arr))
    
    return B


arr = [1,2,3,4,5,6,7,8,9]
B = minimal_tree(arr)
B.printTree()

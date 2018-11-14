'''
Write function to find kth to last element of a linked list
'''

from SingleyLinkedList import LinkedList

def find_kth_to_last(input):
    lst, k = input

    node2 = lst.head
    for i in range(k):
        if node2.next == None:
            return False
        node2 = node2.next
        
    curNode = lst.head

    while node2.next != None:
        curNode = curNode.next
        node2 = node2.next

    return curNode.value
        

lst1 = LinkedList()
for i in range(10):
    lst1.insertNodeAtEnd(i)

tests = [
{"input":  (lst1, 2), "answer": 7},
{"input":  (lst1, 4), "answer": 5},
{"input":  (lst1, 10), "answer": 0},
]

for test in tests:
    q1, a1 = test["input"], find_kth_to_last(test["input"])
    assert a1 == test["answer"]
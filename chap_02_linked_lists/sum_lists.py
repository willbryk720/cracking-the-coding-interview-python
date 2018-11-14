'''
Sum two lists where each list represents number ( 1 -> 5 -> 9 represents 951)

Could do this using recursion
'''

from SingleyLinkedList import LinkedList, Node

# returns the list that represents the sum of two linked lists
def sum_lists(input):
    lst1, lst2 = input
    head = sum_lists_rec(lst1.head, lst2.head, False)

    new_list = LinkedList()
    while head != None:
        new_list.insertNodeAtEnd(head.value)
        head = head.next
    return new_list


# returns copy of list given the head of a list
def copy_list(head):
    if head == None:
        return None

    copy_list = LinkedList()

    while head != None:
        copy_list.insertNodeAtEnd(head.value)
        head = head.next

    return copy_list
        

def sum_lists_rec(head1, head2, hasCarry):
    if head1 == None and head2 == None:
        return Node(1) if hasCarry else None
    elif head1 == None:
        if hasCarry:
            new_node_val = head2.value + 1
            if new_node_val == 10:
                new_node = Node(0)
                new_node.next = sum_lists_rec(head1, head2.next, True)
                return new_node
            else:
                new_node = Node(new_node_val)
                new_node.next = copy_list(head2.next).head
                return new_node
        else:
            return copy_list(head2).head
    elif head2 == None:
        return sum_lists_rec(head2, head1, hasCarry)
    
    sum_val = head1.value + head2.value + (1 if hasCarry else 0)
    new_node = Node(sum_val % 10)
    new_node.next = sum_lists_rec(head1.next, head2.next, sum_val >= 10)
    return new_node 



def getListFromNumString(num_string):
    lst = LinkedList()
    for c in num_string[::-1]:
        lst.insertNodeAtEnd(int(c))
    return lst
    

def checkSolution(num_string1, num_string2):
    lst1 = getListFromNumString(num_string1)
    lst2 = getListFromNumString(num_string2)

    summed_list = sum_lists((lst1, lst2))
    num_string_sum = "".join(str(x) for x in summed_list.getList()[::-1])

    is_correct = int(num_string1) + int(num_string2) == int(num_string_sum)

    print num_string1, "+", num_string2, "=", num_string_sum + "?", is_correct
    return is_correct




assert checkSolution("95", "43")
assert checkSolution("4", "3")
assert checkSolution("9", "162234")
assert checkSolution("95111", "162")
assert checkSolution("9", "3")


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List must have at least two nodes.")
    
    dummy1 = Node(0)
    dummy2 = Node(0)

    tail1 = dummy1
    tail2 = dummy2

    curr = head
    flag = True

    while curr:
        new_node = curr.next
        curr.next = None

        if flag:
            tail1.next = curr
            tail1 = tail1.next
        else:
            tail2.next = curr
            tail2 = tail2.next 

        flag = not flag

        curr = new_node     

    return Context(dummy1.next, dummy2.next)   


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    node = Node(data)

    if head is None or data < head.data:
        node.next = head
        return node
    
    curr = head
    while curr.next is not None and curr.next.data < data:
        curr = curr.next
    
    node.next = curr.next
    curr.next = node

    return head
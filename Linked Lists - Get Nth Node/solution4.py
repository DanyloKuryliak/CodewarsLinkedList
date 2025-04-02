
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    v = -1
    n = node
    while n:
        v += 1
        if v == index:
            return n
        n = n.next
    
    raise ValueError
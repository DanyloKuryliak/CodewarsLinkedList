class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def push(head, data):
    return Node(data, head)

def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
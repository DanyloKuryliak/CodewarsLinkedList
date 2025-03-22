class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s == "None":
        return None

    values = s.split(' -> ')[:-1]
    values = [int(v) for v in values]

    head = None
    for val in reversed(values):
        head = Node(val, head)
    return head
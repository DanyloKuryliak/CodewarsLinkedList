
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = first.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return dummy.next
def loop_size(node):
    slow, fast = node, node

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next

        if slow == fast:
            temp = slow
            count = 1
            while temp.next != slow:
                count += 1
                temp = temp.next
            return count
    return 0
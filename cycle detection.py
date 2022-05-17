def has_cycle(head):
    while head:
        if head.data == 0.5:
            return 1
        head.data = 0.5
        head = head.next
    return 0

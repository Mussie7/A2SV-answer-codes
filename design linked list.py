class Node:
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.ind = 0

    def get(self, index: int) -> int:
        if index >= self.ind:
            return -1
        
        cur = self.head
        while cur:
            if cur.val[0] == index:
                return cur.val[1]
            cur = cur.next

    def addAtHead(self, val: int) -> None:
        new_head = Node([0,val], self.head)
        self.head = new_head
        
        if not self.tail:
            self.tail = self.head
            
        cur = self.head.next
        while cur:
            cur.val[0] += 1
            cur = cur.next
        self.ind += 1

    def addAtTail(self, val: int) -> None:
        new_tail = Node([self.ind,val])
        
        if not self.tail:
            self.tail = new_tail
            self.head = self.tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        self.ind += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node([index,val])

        if index == 0:
            return self.addAtHead(val)
        elif index == self.ind:
            return self.addAtTail(val)
        elif index > self.ind:
            return
        
        cur = self.head
        while cur.next:
            if cur.next.val[0] == index:
                new_node.next = cur.next
                cur.next = new_node
                break
            cur = cur.next
        print(cur.val)
        cur = cur.next.next
        while cur:
            cur.val[0] += 1
            cur = cur.next
        
        self.ind += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head

        if index >= self.ind:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            while cur.next:
                if index == cur.next.val[0]:
                    cur.next = cur.next.next
                    if index == self.ind - 1:
                        self.tail = cur
                    break
                cur = cur.next
            
            cur = cur.next
        while cur:
            cur.val[0] -= 1
            cur = cur.next
        self.ind -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

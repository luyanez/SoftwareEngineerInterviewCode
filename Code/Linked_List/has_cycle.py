class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add_node_end(self, value):
        h = self
        nextval = ListNode(value)
        while h.next != None:
            h = h.next
        h.next = nextval

    def print_linkedList(self):
        h = self
        while h:
            print(h.val)
            h = h.next  

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

head = ListNode(1)
head.add_node_end(2)
head.add_node_end(3)
head.add_node_end(4)
head.add_node_end(5)
head.print_linkedList()

ans = has_cycle()
print("Does linked link has cycle: ",ans)



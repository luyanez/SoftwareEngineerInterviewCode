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

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val

head = ListNode(1)
head.add_node_end(2)
head.add_node_end(3)
head.add_node_end(4)
head.add_node_end(5)
#head.print_linkedList()

ans = get_middle(head)
print("The value of the middle node is: ",ans)


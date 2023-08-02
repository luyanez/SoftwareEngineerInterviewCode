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

def return_k_from_end(head, k):
    slow = head
    fast = head

    for i in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.val

head = ListNode(1)
head.add_node_end(2)
head.add_node_end(3)
head.add_node_end(4)
head.add_node_end(5)

k = 2
ans = return_k_from_end(head, k)
print("The k node from the end is: ",ans)
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

def swap_nodes_in_pairs(head):
    if not head or not head.next:
        return head
    
    dummy = head.next
    prev = None

    while head and head.next:
        if prev:
            prev.next = head.next

        prev = head

        next_node = head.next.next
        head.next.next = head

        head.next = next_node
        head = next_node

    return dummy

head = ListNode(1)
head.add_node_end(2)
head.add_node_end(3)
head.add_node_end(4)
head.add_node_end(5)
head.add_node_end(6)

ans = swap_nodes_in_pairs(head)
ans.print_linkedList()
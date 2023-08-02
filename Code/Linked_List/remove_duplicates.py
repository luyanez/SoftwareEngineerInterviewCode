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

def remove_duplicates(head):
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head

head = ListNode(1)
head.add_node_end(1)
head.add_node_end(1)
head.add_node_end(2)
head.add_node_end(2)

ans = remove_duplicates(head)
ans.print_linkedList()

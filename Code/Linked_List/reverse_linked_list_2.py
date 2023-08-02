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

def reverse_list_2(head, m, n):
    # Empty list
    if not head:
        return None

    # Move the two pointers until they reach the proper starting point
    # in the list.
    cur, prev = head, None
    while m > 1:
        prev = cur
        cur = cur.next
        m, n = m - 1, n - 1

    # The two pointers that will fix the final connections.
    tail, con = cur, prev

    # Iteratively reverse the nodes until n becomes 0.
    while n:
        third = cur.next
        cur.next = prev
        prev = cur
        cur = third
        n -= 1

    # Adjust the final connections as explained in the algorithm
    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur

    return head



head = ListNode(7)
head.add_node_end(9)
head.add_node_end(2)
head.add_node_end(10)
head.add_node_end(1)
head.add_node_end(8)
head.add_node_end(6)

ans = reverse_list_2(head, 3, 6)
ans.print_linkedList()

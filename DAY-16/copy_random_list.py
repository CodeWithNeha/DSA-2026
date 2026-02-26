class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def copyRandomList(head):
    if not head:
        return None

    # Step 1: clone nodes
    curr = head
    while curr:
        newNode = ListNode(curr.val)
        newNode.next = curr.next
        curr.next = newNode
        curr = newNode.next

    # Step 2: copy random
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: separate lists
    curr = head
    dummy = ListNode(0)
    copy = dummy

    while curr:
        copy.next = curr.next
        curr.next = curr.next.next
        curr = curr.next
        copy = copy.next

    return dummy.next
class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    dummy = LinkedList()
    curr = dummy 

    for val in arr:
        curr.next = LinkedList(val)
        curr = curr.next

    return dummy.next

head = create_linked_list([1,2,3,4,5])


def reverseLinkedList(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

head = reverseLinkedList(head)

while head:
    print(head.val)
    head = head.next
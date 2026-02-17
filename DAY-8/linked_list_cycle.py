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

def hadCycle(head):
    slow=fast=head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print(hadCycle(head))
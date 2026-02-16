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


def reverseLinkedList(head, left, right):
    if not head or left==right:
        return head
    
    dummy = LinkedList(0, head)
    prev = dummy

    for _ in range(left-1):
        prev = prev.next
    curr = prev.next
    for _ in range(right-left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next

head = reverseLinkedList(head, left=2,right=4)

while head:
    print(head.val)
    head = head.next
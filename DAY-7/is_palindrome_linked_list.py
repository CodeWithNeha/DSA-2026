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

head = create_linked_list([1,2,2,1])


def isPalindrome(head):
    if not head or not head.next:
        return True
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


    

print(isPalindrome(head))

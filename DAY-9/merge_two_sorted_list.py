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

head1 = create_linked_list([1,2,3,6,9])
head2 = create_linked_list([4,5,7,8])

def mergeTwoLists(head1, head2):
    dummy = LinkedList(0)
    curr = dummy

    while head1 and head2:
        if head1.val < head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    curr.next = head1 or head2
    return dummy.next
    

head3 = mergeTwoLists(head1, head2)
while head3:
    print(head3.val)
    head3 = head3.next
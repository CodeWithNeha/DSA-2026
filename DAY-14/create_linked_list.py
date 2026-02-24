class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(li):
    head = ListNode(li[0])
    curr = head
    for x in range(1,len(li)):
        curr.next = ListNode(li[x])
        curr = curr.next

    return head

head = create_list([1,2,3,4])
while head:
    print(head.val, end="-> ")
    head = head.next
print(head)
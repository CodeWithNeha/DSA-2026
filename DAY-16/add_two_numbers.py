class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumber(l1,l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total%10)
        curr = curr.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy


def create_list(li):
    head = ListNode(li[0])
    curr = head
    for x in range(1,len(li)):
        curr.next = ListNode(li[x])
        curr = curr.next

    return head

head = create_list([2,4,3])
head2 = create_list([5,6,4])

head3 = addTwoNumber(head,head2)
while head3:
    print(head3.val, end="-> ")
    head3 = head3.next
# print(head3)
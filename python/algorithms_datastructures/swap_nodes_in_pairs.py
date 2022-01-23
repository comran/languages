# LC 24

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    first_head = first = ListNode()
    second_head = second = ListNode()
    p = head
    is_first = True

    while p:
        if is_first:
            first.next = p
            first = first.next
        else:
            second.next = p
            second = second.next

        is_first = not is_first
        p = p.next

    first.next = None
    second.next = None

    first = first_head.next
    second = second_head.next
    head = p = ListNode()
    is_first = False
    while first and second:
        if is_first:
            p.next = first
            first = first.next
        else:
            p.next = second
            second = second.next
        is_first = not is_first
        p = p.next

    if first:
        p.next = first

    if second:
        p.next = second

    return head.next


################################################################################
# Test cases.

tst = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

tst_result = swapPairs(tst)
tst_result_list = []

while tst_result:
    tst_result_list.append(tst_result.val)
    tst_result = tst_result.next

assert tst_result_list == [2, 1, 4, 3]

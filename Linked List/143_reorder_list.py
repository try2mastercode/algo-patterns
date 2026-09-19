class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first, second = head, prev
        while second:
            n1, n2 = first.next, second.next
            first.next = second
            second.next = n1
            first, second = n1, n2


def build(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


sol = Solution()
l1 = build([1, 2, 3, 4])
sol.reorderList(l1)
assert to_list(l1) == [1, 4, 2, 3]

l2 = build([1, 2, 3, 4, 5])
sol.reorderList(l2)
assert to_list(l2) == [1, 5, 2, 4, 3]

l3 = build([1])
sol.reorderList(l3)
assert to_list(l3) == [1]
print("All tests passed")

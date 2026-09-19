class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head


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
assert to_list(sol.oddEvenList(build([1, 2, 3, 4, 5]))) == [1, 3, 5, 2, 4]
assert to_list(sol.oddEvenList(build([2, 1, 3, 5, 6, 4, 7]))) == [2, 3, 6, 7, 1, 5, 4]
assert to_list(sol.oddEvenList(build([]))) == []
print("All tests passed")

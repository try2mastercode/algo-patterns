class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


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
assert to_list(sol.reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
assert to_list(sol.reverseList(build([1, 2]))) == [2, 1]
assert to_list(sol.reverseList(build([]))) == []
print("All tests passed")

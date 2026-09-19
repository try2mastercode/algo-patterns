class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]


def build(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


sol = Solution()
assert sol.isPalindrome(build([1, 2, 2, 1])) is True
assert sol.isPalindrome(build([1, 2])) is False
assert sol.isPalindrome(build([1])) is True
print("All tests passed")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry, digit = divmod(total, 10)
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


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
assert to_list(sol.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))) == [7, 0, 8]
assert to_list(sol.addTwoNumbers(build([0]), build([0]))) == [0]
assert to_list(sol.addTwoNumbers(build([9, 9, 9]), build([1]))) == [0, 0, 0, 1]
print("All tests passed")

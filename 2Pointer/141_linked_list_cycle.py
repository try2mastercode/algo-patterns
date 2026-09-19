class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


sol = Solution()

a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
a.next, b.next, c.next, d.next = b, c, d, b
assert sol.hasCycle(a) is True

x, y, z = ListNode(1), ListNode(2), ListNode(3)
x.next, y.next = y, z
assert sol.hasCycle(x) is False

assert sol.hasCycle(None) is False
print("All tests passed")

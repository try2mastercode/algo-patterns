class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        tail.next = head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head


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
assert to_list(sol.rotateRight(build([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
assert to_list(sol.rotateRight(build([0, 1, 2]), 4)) == [2, 0, 1]
assert to_list(sol.rotateRight(build([]), 5)) == []
print("All tests passed")

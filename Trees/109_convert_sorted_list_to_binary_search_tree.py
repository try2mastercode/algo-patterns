class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head):
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi + 1) // 2
            root = TreeNode(values[mid])
            root.left = build(lo, mid - 1)
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(values) - 1)


def build_list(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))


sol = Solution()
tree = sol.sortedListToBST(build_list([-10, -3, 0, 5, 9]))
assert inorder(tree) == [-10, -3, 0, 5, 9]
assert abs(height(tree.left) - height(tree.right)) <= 1
assert sol.sortedListToBST(None) is None
print("All tests passed")

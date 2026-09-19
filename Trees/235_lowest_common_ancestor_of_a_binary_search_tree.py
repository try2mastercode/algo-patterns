class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


sol = Solution()
n2, n8 = TreeNode(2), TreeNode(8)
n0, n4, n7, n9 = TreeNode(0), TreeNode(4), TreeNode(7), TreeNode(9)
n3, n5 = TreeNode(3), TreeNode(5)
n4.left, n4.right = n3, n5
n8.left, n8.right = n7, n9
root = TreeNode(6, TreeNode(2, n0, n4), n8)
root.left = TreeNode(2, n0, n4)

assert sol.lowestCommonAncestor(root, root.left, n8).val == 6
assert sol.lowestCommonAncestor(root, root.left, n4).val == 2
assert sol.lowestCommonAncestor(TreeNode(1, None, TreeNode(2)), TreeNode(1), TreeNode(2)).val == 1
print("All tests passed")

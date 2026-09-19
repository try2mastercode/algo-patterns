class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def depth(node):
            nonlocal diameter
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return diameter


sol = Solution()
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
assert sol.diameterOfBinaryTree(root1) == 3

root2 = TreeNode(1, TreeNode(2))
assert sol.diameterOfBinaryTree(root2) == 1

assert sol.diameterOfBinaryTree(TreeNode(1)) == 0
print("All tests passed")

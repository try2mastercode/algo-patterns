class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1


sol = Solution()
assert sol.isBalanced(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) is True
assert sol.isBalanced(
    TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(3)), TreeNode(2))
) is False
assert sol.isBalanced(None) is True
print("All tests passed")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root):
        def dfs(node, curr):
            if not node:
                return 0
            curr = curr * 10 + node.val
            if not node.left and not node.right:
                return curr
            return dfs(node.left, curr) + dfs(node.right, curr)

        return dfs(root, 0)


sol = Solution()
assert sol.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))) == 25
assert sol.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))) == 1026
print("All tests passed")

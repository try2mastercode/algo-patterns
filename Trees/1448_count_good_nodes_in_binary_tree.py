class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root):
        def dfs(node, max_so_far):
            if not node:
                return 0
            count = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)
            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)
            return count

        return dfs(root, root.val)


sol = Solution()
root1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
assert sol.goodNodes(root1) == 4

root2 = TreeNode(3, TreeNode(3, None, TreeNode(4)), TreeNode(2))
assert sol.goodNodes(root2) == 3

assert sol.goodNodes(TreeNode(1)) == 1
print("All tests passed")

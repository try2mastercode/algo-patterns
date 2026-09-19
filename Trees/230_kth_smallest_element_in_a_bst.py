class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


sol = Solution()
tree1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
assert sol.kthSmallest(tree1, 1) == 1

tree2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
assert sol.kthSmallest(tree2, 3) == 3

assert sol.kthSmallest(TreeNode(1), 1) == 1
print("All tests passed")

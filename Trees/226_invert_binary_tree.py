class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


def to_preorder(node):
    if not node:
        return []
    return [node.val] + to_preorder(node.left) + to_preorder(node.right)


sol = Solution()
tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted = sol.invertTree(tree)
assert to_preorder(inverted) == [4, 7, 9, 6, 2, 3, 1]
assert sol.invertTree(None) is None
assert to_preorder(sol.invertTree(TreeNode(1))) == [1]
print("All tests passed")

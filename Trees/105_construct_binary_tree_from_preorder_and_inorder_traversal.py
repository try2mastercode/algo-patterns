class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root


def to_preorder(node):
    if not node:
        return []
    return [node.val] + to_preorder(node.left) + to_preorder(node.right)


sol = Solution()
tree = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
assert to_preorder(tree) == [3, 9, 20, 15, 7]

tree2 = sol.buildTree([-1], [-1])
assert to_preorder(tree2) == [-1]

tree3 = sol.buildTree([1, 2], [2, 1])
assert to_preorder(tree3) == [1, 2]
print("All tests passed")

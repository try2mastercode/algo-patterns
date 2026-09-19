class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right


def to_list(root):
    res = []
    node = root
    while node:
        res.append(node.val)
        assert node.left is None
        node = node.right
    return res


sol = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
sol.flatten(root)
assert to_list(root) == [1, 2, 3, 4, 5, 6]

root2 = TreeNode(1)
sol.flatten(root2)
assert to_list(root2) == [1]
print("All tests passed")

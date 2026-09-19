class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


sol = Solution()
assert sol.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))) is True
assert sol.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))) is False
assert sol.isSameTree(None, None) is True
print("All tests passed")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("N")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = iter(data.split(","))

        def build():
            val = next(vals)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()


def to_preorder(node):
    if not node:
        return []
    return [node.val] + to_preorder(node.left) + to_preorder(node.right)


codec = Codec()
tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
restored = codec.deserialize(codec.serialize(tree))
assert to_preorder(restored) == [1, 2, 3, 4, 5]
assert codec.deserialize(codec.serialize(None)) is None
assert to_preorder(codec.deserialize(codec.serialize(TreeNode(1)))) == [1]
print("All tests passed")

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        old_to_new = {}
        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            old_to_new[node].next = old_to_new.get(node.next)
            old_to_new[node].random = old_to_new.get(node.random)
            node = node.next
        return old_to_new[head]


def build(pairs):
    nodes = [Node(v) for v, _ in pairs]
    for i, (_, rand_idx) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0] if nodes else None


def to_pairs(head):
    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next
    index = {n: i for i, n in enumerate(nodes)}
    return [(n.val, index[n.random] if n.random else None) for n in nodes]


sol = Solution()
data = [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
copied = sol.copyRandomList(build(data))
assert to_pairs(copied) == data
assert sol.copyRandomList(None) is None
assert to_pairs(sol.copyRandomList(build([(1, 0)]))) == [(1, 0)]
print("All tests passed")

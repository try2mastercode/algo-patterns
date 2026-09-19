class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        clones = {}

        def dfs(n):
            if n in clones:
                return clones[n]
            copy = Node(n.val)
            clones[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)


def build(adj):
    nodes = {i: Node(i) for i in adj}
    for i, neighbors in adj.items():
        nodes[i].neighbors = [nodes[j] for j in neighbors]
    return nodes[1] if nodes else None


def to_adj(node):
    visited = {}

    def dfs(n):
        if n.val in visited:
            return
        visited[n.val] = sorted(nei.val for nei in n.neighbors)
        for nei in n.neighbors:
            dfs(nei)

    dfs(node)
    return visited


sol = Solution()
graph = build({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
cloned = sol.cloneGraph(graph)
assert to_adj(cloned) == {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
assert sol.cloneGraph(None) is None
single = build({1: []})
assert to_adj(sol.cloneGraph(single)) == {1: []}
print("All tests passed")

class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        return all(union(u, v) for u, v in edges)


sol = Solution()
assert sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
assert sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
assert sol.validTree(1, []) is True
print("All tests passed")

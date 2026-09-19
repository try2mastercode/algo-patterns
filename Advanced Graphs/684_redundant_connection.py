class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            rank[rx] += rank[ry]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []


sol = Solution()
assert sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
print("All tests passed")

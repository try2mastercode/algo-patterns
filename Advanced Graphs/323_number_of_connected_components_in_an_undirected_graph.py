class Solution:
    def countComponents(self, n, edges):
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

        count = n
        for u, v in edges:
            if union(u, v):
                count -= 1
        return count


sol = Solution()
assert sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
assert sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
assert sol.countComponents(3, []) == 3
print("All tests passed")

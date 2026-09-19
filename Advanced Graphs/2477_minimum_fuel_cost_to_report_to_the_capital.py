class Solution:
    def minimumFuelCost(self, roads, seats):
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        total = 0

        def dfs(node, parent):
            nonlocal total
            size = 1
            for neighbor in graph[node]:
                if neighbor != parent:
                    size += dfs(neighbor, node)
            if node != 0:
                total += -(-size // seats)
            return size

        dfs(0, -1)
        return total


sol = Solution()
assert sol.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) == 3
assert sol.minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) == 7
assert sol.minimumFuelCost([], 1) == 0
print("All tests passed")

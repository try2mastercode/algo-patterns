class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            updated = prices[:]
            for u, v, w in flights:
                if prices[u] != float("inf") and prices[u] + w < updated[v]:
                    updated[v] = prices[u] + w
            prices = updated

        return prices[dst] if prices[dst] != float("inf") else -1


sol = Solution()
assert sol.findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1) == 700
assert sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200
assert sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500
print("All tests passed")

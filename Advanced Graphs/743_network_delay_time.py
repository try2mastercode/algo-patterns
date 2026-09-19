import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}
        heap = [(0, k)]
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d + w, nei))

        return max(dist.values()) if len(dist) == n else -1


sol = Solution()
assert sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
assert sol.networkDelayTime([[1, 2, 1]], 2, 1) == 1
assert sol.networkDelayTime([[1, 2, 1]], 2, 2) == -1
print("All tests passed")

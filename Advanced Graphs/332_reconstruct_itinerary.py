from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            while graph[airport]:
                dfs(heapq.heappop(graph[airport]))
            route.append(airport)

        dfs("JFK")
        return route[::-1]


sol = Solution()
assert sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == [
    "JFK", "MUC", "LHR", "SFO", "SJC"
]
assert sol.findItinerary(
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
print("All tests passed")

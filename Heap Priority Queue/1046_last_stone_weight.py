import heapq


class Solution:
    def lastStoneWeight(self, stones):
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if y != x:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0


sol = Solution()
assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
assert sol.lastStoneWeight([1]) == 1
assert sol.lastStoneWeight([2, 2]) == 0
print("All tests passed")

import heapq


class Solution:
    def kClosest(self, points, k):
        heap = [(x * x + y * y, x, y) for x, y in points]
        heapq.heapify(heap)
        return [[x, y] for _, x, y in heapq.nsmallest(k, heap)]


sol = Solution()
assert sol.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
assert sorted(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == sorted([[3, 3], [-2, 4]])
assert sol.kClosest([[0, 0]], 1) == [[0, 0]]
print("All tests passed")

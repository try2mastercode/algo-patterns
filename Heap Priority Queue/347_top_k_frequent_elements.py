import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        return [num for num, _ in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]


sol = Solution()
assert set(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
assert sol.topKFrequent([1], 1) == [1]
assert set(sol.topKFrequent([4, 4, 4, 1, 1, 2], 2)) == {4, 1}
print("All tests passed")

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        removed = 0
        prev_end = float("-inf")
        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removed += 1
        return removed


sol = Solution()
assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
print("All tests passed")

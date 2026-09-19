class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        lengths = [1] * n
        counts = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == longest)


sol = Solution()
assert sol.findNumberOfLIS([1, 3, 5, 4, 7]) == 2
assert sol.findNumberOfLIS([2, 2, 2, 2, 2]) == 5
assert sol.findNumberOfLIS([1]) == 1
print("All tests passed")

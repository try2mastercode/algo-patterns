class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


sol = Solution()
assert sol.missingNumber([3, 0, 1]) == 2
assert sol.missingNumber([0, 1]) == 2
assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
print("All tests passed")

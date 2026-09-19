class Solution:
    def maxSubArray(self, nums):
        curr_sum = nums[0]
        best = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            best = max(best, curr_sum)
        return best


sol = Solution()
assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert sol.maxSubArray([1]) == 1
assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
print("All tests passed")

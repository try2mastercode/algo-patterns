class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in memo:
                return memo[(i, total)]
            res = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            memo[(i, total)] = res
            return res

        return backtrack(0, 0)


sol = Solution()
assert sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
assert sol.findTargetSumWays([1], 1) == 1
assert sol.findTargetSumWays([1, 0], 1) == 2
print("All tests passed")

class Solution:
    def rob(self, nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr


sol = Solution()
assert sol.rob([1, 2, 3, 1]) == 4
assert sol.rob([2, 7, 9, 3, 1]) == 12
assert sol.rob([]) == 0
assert sol.rob([5]) == 5
print("All tests passed")

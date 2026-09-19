class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev, curr = 0, 0
            for num in houses:
                prev, curr = curr, max(curr, prev + num)
            return curr

        return max(rob_line(nums[1:]), rob_line(nums[:-1]))


sol = Solution()
assert sol.rob([2, 3, 2]) == 3
assert sol.rob([1, 2, 3, 1]) == 4
assert sol.rob([1, 2, 3]) == 3
assert sol.rob([5]) == 5
print("All tests passed")

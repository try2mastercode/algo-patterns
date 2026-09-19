class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


sol = Solution()
assert sol.canJump([2, 3, 1, 1, 4]) is True
assert sol.canJump([3, 2, 1, 0, 4]) is False
assert sol.canJump([0]) is True
print("All tests passed")

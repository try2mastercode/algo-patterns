class Solution:
    def jump(self, nums):
        jumps = 0
        cur_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest
        return jumps


sol = Solution()
assert sol.jump([2, 3, 1, 1, 4]) == 2
assert sol.jump([2, 3, 0, 1, 4]) == 2
assert sol.jump([1]) == 0
print("All tests passed")

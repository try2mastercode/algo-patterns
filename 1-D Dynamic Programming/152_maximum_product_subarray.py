class Solution:
    def maxProduct(self, nums):
        res = nums[0]
        cur_max, cur_min = 1, 1
        for num in nums:
            candidates = (num, cur_max * num, cur_min * num)
            cur_max, cur_min = max(candidates), min(candidates)
            res = max(res, cur_max)
        return res


sol = Solution()
assert sol.maxProduct([2, 3, -2, 4]) == 6
assert sol.maxProduct([-2, 0, -1]) == 0
assert sol.maxProduct([-2, 3, -4]) == 24
print("All tests passed")

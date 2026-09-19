class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]


sol = Solution()
assert sol.findMin([3, 4, 5, 1, 2]) == 1
assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
assert sol.findMin([11, 13, 15, 17]) == 11
assert sol.findMin([1]) == 1
print("All tests passed")

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


sol = Solution()
assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
assert sol.search([5], 5) == 0
print("All tests passed")

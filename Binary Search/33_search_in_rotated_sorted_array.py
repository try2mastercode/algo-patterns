class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


sol = Solution()
assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert sol.search([1], 0) == -1
assert sol.search([1], 1) == 0
print("All tests passed")

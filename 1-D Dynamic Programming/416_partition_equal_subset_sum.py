class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = {0}
        for num in nums:
            dp |= {num + s for s in dp if num + s <= target}
        return target in dp


sol = Solution()
assert sol.canPartition([1, 5, 11, 5]) is True
assert sol.canPartition([1, 2, 3, 5]) is False
assert sol.canPartition([1, 1]) is True
print("All tests passed")

class Solution:
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


sol = Solution()
assert sol.countBits(2) == [0, 1, 1]
assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
assert sol.countBits(0) == [0]
print("All tests passed")

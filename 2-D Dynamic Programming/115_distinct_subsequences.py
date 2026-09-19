class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[m][n]


sol = Solution()
assert sol.numDistinct("rabbbit", "rabbit") == 3
assert sol.numDistinct("babgbag", "bag") == 5
assert sol.numDistinct("a", "b") == 0
print("All tests passed")

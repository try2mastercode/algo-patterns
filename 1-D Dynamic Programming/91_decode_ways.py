class Solution:
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        return dp[n]


sol = Solution()
assert sol.numDecodings("12") == 2
assert sol.numDecodings("226") == 3
assert sol.numDecodings("06") == 0
assert sol.numDecodings("0") == 0
print("All tests passed")

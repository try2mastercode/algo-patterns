class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]


sol = Solution()
assert sol.change(5, [1, 2, 5]) == 4
assert sol.change(3, [2]) == 0
assert sol.change(10, [10]) == 1
assert sol.change(0, []) == 1
print("All tests passed")

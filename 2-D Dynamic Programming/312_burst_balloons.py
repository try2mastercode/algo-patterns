class Solution:
    def maxCoins(self, nums):
        balloons = [1] + nums + [1]
        n = len(balloons)
        memo = {}

        def dp(l, r):
            if l + 1 == r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            best = 0
            for i in range(l + 1, r):
                coins = balloons[l] * balloons[i] * balloons[r] + dp(l, i) + dp(i, r)
                best = max(best, coins)
            memo[(l, r)] = best
            return best

        return dp(0, n - 1)


sol = Solution()
assert sol.maxCoins([3, 1, 5, 8]) == 167
assert sol.maxCoins([1, 5]) == 10
assert sol.maxCoins([]) == 0
print("All tests passed")

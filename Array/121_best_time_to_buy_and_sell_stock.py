class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best, price - min_price)
        return best


sol = Solution()
assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
assert sol.maxProfit([2, 4, 1]) == 2
print("All tests passed")

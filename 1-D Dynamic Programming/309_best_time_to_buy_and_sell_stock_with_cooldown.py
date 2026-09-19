class Solution:
    def maxProfit(self, prices):
        sold, held, rest = float("-inf"), float("-inf"), 0
        for price in prices:
            prev_sold = sold
            sold = held + price
            held = max(held, rest - price)
            rest = max(rest, prev_sold)
        return max(sold, rest)


sol = Solution()
assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
assert sol.maxProfit([1]) == 0
assert sol.maxProfit([1, 2, 4]) == 3
print("All tests passed")

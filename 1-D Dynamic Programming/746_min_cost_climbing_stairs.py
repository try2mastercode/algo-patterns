class Solution:
    def minCostClimbingStairs(self, cost):
        prev, curr = 0, 0
        for i in range(2, len(cost) + 1):
            prev, curr = curr, min(curr + cost[i - 1], prev + cost[i - 2])
        return curr


sol = Solution()
assert sol.minCostClimbingStairs([10, 15, 20]) == 15
assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
assert sol.minCostClimbingStairs([0, 0, 0, 1]) == 0
print("All tests passed")

class Solution:
    def climbStairs(self, n):
        prev, curr = 1, 1
        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        return curr


sol = Solution()
assert sol.climbStairs(2) == 2
assert sol.climbStairs(3) == 3
assert sol.climbStairs(1) == 1
assert sol.climbStairs(5) == 8
print("All tests passed")

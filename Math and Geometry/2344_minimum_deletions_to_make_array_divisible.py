from math import gcd
from functools import reduce


class Solution:
    def minOperations(self, nums, numsDivide):
        g = reduce(gcd, numsDivide)
        candidates = sorted(x for x in nums if g % x == 0)
        if not candidates:
            return -1
        smallest = candidates[0]
        return sum(1 for x in nums if x < smallest)


sol = Solution()
assert sol.minOperations([2, 3, 2, 4, 3], [9, 6, 9, 3, 15]) == 2
assert sol.minOperations([4, 3, 6], [8, 2, 6, 10]) == -1
assert sol.minOperations([2, 4, 8], [2]) == 0
print("All tests passed")

from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums):
        return reduce(xor, nums, 0)


sol = Solution()
assert sol.singleNumber([2, 2, 1]) == 1
assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
assert sol.singleNumber([1]) == 1
print("All tests passed")

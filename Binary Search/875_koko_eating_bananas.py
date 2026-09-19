import math


class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            hours = sum(math.ceil(pile / k) for pile in piles)
            if hours <= h:
                r = k
            else:
                l = k + 1
        return l


sol = Solution()
assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
print("All tests passed")

class Solution:
    def mergeTriplets(self, triplets, target):
        good = set()
        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                for i, v in enumerate((x, y, z)):
                    if v == target[i]:
                        good.add(i)
        return len(good) == 3


sol = Solution()
assert sol.mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]) is True
assert sol.mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]) is False
assert sol.mergeTriplets([[3, 4, 5]], [5, 5, 5]) is False
print("All tests passed")

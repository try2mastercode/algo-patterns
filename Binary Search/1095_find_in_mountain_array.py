class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        return self.arr[index]

    def length(self):
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()

        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                lo = mid + 1
            else:
                hi = mid
        peak = lo

        lo, hi = 0, peak
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        lo, hi = peak, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


sol = Solution()
assert sol.findInMountainArray(3, MountainArray([1, 2, 3, 4, 5, 3, 1])) == 2
assert sol.findInMountainArray(0, MountainArray([0, 1, 2, 4, 2, 1])) == 0
assert sol.findInMountainArray(3, MountainArray([1, 5, 2])) == -1
print("All tests passed")

class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            width = r - l
            best = max(best, width * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best


sol = Solution()
assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert sol.maxArea([1, 1]) == 1
assert sol.maxArea([4, 3, 2, 1, 4]) == 16
print("All tests passed")

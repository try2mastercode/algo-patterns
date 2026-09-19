class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area


sol = Solution()
assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
assert sol.largestRectangleArea([2, 4]) == 4
assert sol.largestRectangleArea([1]) == 1
print("All tests passed")

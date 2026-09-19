class Solution:
    def searchMatrix(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            m = (l + r) // 2
            val = matrix[m // cols][m % cols]
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        return False


sol = Solution()
assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
assert sol.searchMatrix([[1]], 1) is True
print("All tests passed")

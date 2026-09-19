class Solution:
    def uniquePaths(self, m, n):
        row = [1] * n
        for _ in range(m - 1):
            new_row = [1] * n
            for c in range(n - 2, -1, -1):
                new_row[c] = new_row[c + 1] + row[c]
            row = new_row
        return row[0]


sol = Solution()
assert sol.uniquePaths(3, 7) == 28
assert sol.uniquePaths(3, 2) == 3
assert sol.uniquePaths(1, 1) == 1
print("All tests passed")

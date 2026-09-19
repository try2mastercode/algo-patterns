class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0


sol = Solution()
m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
sol.setZeroes(m1)
assert m1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
sol.setZeroes(m2)
assert m2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
print("All tests passed")

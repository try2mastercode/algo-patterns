class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()


sol = Solution()
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(m1)
assert m1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

m2 = [[1]]
sol.rotate(m2)
assert m2 == [[1]]

m3 = [[1, 2], [3, 4]]
sol.rotate(m3)
assert m3 == [[3, 1], [4, 2]]
print("All tests passed")

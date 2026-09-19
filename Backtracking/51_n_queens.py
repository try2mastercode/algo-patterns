class Solution:
    def solveNQueens(self, n):
        res = []
        cols = set()
        diag = set()
        anti_diag = set()
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in anti_diag:
                    continue
                cols.add(col)
                diag.add(row - col)
                anti_diag.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                diag.remove(row - col)
                anti_diag.remove(row + col)
                board[row][col] = "."

        backtrack(0)
        return res


sol = Solution()
assert len(sol.solveNQueens(4)) == 2
assert len(sol.solveNQueens(1)) == 1
assert sol.solveNQueens(2) == []
print("All tests passed")

from collections import deque

INF = 2147483647


class Solution:
    def islandsAndTreasure(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))


sol = Solution()
grid1 = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
sol.islandsAndTreasure(grid1)
assert grid1 == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]

grid2 = [[0]]
sol.islandsAndTreasure(grid2)
assert grid2 == [[0]]
print("All tests passed")

import heapq


class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))


sol = Solution()
assert sol.swimInWater([[0, 2], [1, 3]]) == 3
assert sol.swimInWater(
    [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
) == 16
assert sol.swimInWater([[0]]) == 0
print("All tests passed")

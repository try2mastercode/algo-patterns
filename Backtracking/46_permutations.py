class Solution:
    def permute(self, nums):
        res = []

        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i + 1:])
                path.pop()

        backtrack([], nums)
        return res


sol = Solution()
assert sorted(sol.permute([1, 2, 3])) == sorted(
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
)
assert sorted(sol.permute([0, 1])) == [[0, 1], [1, 0]]
assert sol.permute([1]) == [[1]]
print("All tests passed")

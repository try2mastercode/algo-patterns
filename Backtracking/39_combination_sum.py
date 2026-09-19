class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res


def normalize(combos):
    return sorted(sorted(c) for c in combos)


sol = Solution()
assert normalize(sol.combinationSum([2, 3, 6, 7], 7)) == normalize([[2, 2, 3], [7]])
assert normalize(sol.combinationSum([2, 3, 5], 8)) == normalize([[2, 2, 2, 2], [2, 3, 3], [3, 5]])
assert sol.combinationSum([2], 1) == []
print("All tests passed")

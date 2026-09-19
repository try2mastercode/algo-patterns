class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res


def normalize(combos):
    return sorted(sorted(c) for c in combos)


sol = Solution()
assert normalize(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == normalize(
    [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
)
assert normalize(sol.combinationSum2([2, 5, 2, 1, 2], 5)) == normalize([[1, 2, 2], [5]])
print("All tests passed")

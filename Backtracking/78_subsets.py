class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


def normalize(subs):
    return sorted(sorted(s) for s in subs)


sol = Solution()
assert normalize(sol.subsets([1, 2, 3])) == normalize(
    [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
)
assert sol.subsets([]) == [[]]
assert normalize(sol.subsets([0])) == [[], [0]]
print("All tests passed")

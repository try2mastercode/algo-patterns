class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


def normalize(subs):
    return sorted(sorted(s) for s in subs)


sol = Solution()
assert normalize(sol.subsetsWithDup([1, 2, 2])) == normalize(
    [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
)
assert normalize(sol.subsetsWithDup([0])) == [[], [0]]
print("All tests passed")

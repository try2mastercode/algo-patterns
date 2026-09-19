class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        return res


sol = Solution()
assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
assert sol.merge([[1, 4]]) == [[1, 4]]
print("All tests passed")

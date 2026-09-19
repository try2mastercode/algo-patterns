class Solution:
    def partitionLabels(self, s):
        last = {ch: i for i, ch in enumerate(s)}
        res = []
        start, end = 0, 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res


sol = Solution()
assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert sol.partitionLabels("eccbbbbdec") == [10]
assert sol.partitionLabels("abc") == [1, 1, 1]
print("All tests passed")

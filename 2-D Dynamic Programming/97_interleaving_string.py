class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}

        def dp(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            res = False
            if i < len(s1) and s1[i] == s3[i + j] and dp(i + 1, j):
                res = True
            if not res and j < len(s2) and s2[j] == s3[i + j] and dp(i, j + 1):
                res = True
            memo[(i, j)] = res
            return res

        return dp(0, 0)


sol = Solution()
assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
assert sol.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
assert sol.isInterleave("", "", "") is True
print("All tests passed")

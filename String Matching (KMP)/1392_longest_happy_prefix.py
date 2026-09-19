class Solution:
    def longestPrefix(self, s):
        n = len(s)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return s[:lps[-1]]


sol = Solution()
assert sol.longestPrefix("level") == "l"
assert sol.longestPrefix("ababab") == "abab"
assert sol.longestPrefix("leetcodeleet") == "leet"
print("All tests passed")

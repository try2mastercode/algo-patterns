class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > len(res):
                    res = s[l + 1:r]
        return res


sol = Solution()
assert sol.longestPalindrome("babad") in ("bab", "aba")
assert sol.longestPalindrome("cbbd") == "bb"
assert sol.longestPalindrome("a") == "a"
assert sol.longestPalindrome("") == ""
print("All tests passed")

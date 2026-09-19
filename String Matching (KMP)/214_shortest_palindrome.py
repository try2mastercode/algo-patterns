class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return s
        combined = s + "#" + s[::-1]
        n = len(combined)
        lps = [0] * n
        length = 0
        i = 1
        while i < n:
            if combined[i] == combined[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        to_add = s[lps[-1]:][::-1]
        return to_add + s


sol = Solution()
assert sol.shortestPalindrome("aacecaaa") == "aaacecaaa"
assert sol.shortestPalindrome("abcd") == "dcbabcd"
assert sol.shortestPalindrome("") == ""
print("All tests passed")

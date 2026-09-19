class Solution:
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        return count


sol = Solution()
assert sol.countSubstrings("abc") == 3
assert sol.countSubstrings("aaa") == 6
assert sol.countSubstrings("") == 0
assert sol.countSubstrings("a") == 1
print("All tests passed")

from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


sol = Solution()
assert sol.isAnagram("anagram", "nagaram") is True
assert sol.isAnagram("rat", "car") is False
assert sol.isAnagram("", "") is True
assert sol.isAnagram("a", "ab") is False
print("All tests passed")

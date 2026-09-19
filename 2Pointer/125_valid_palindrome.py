class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True


sol = Solution()
assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
assert sol.isPalindrome("race a car") is False
assert sol.isPalindrome(" ") is True
assert sol.isPalindrome("0P") is False
print("All tests passed")

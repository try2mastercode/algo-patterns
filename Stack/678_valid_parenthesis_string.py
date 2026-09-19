class Solution:
    def checkValidString(self, s):
        lo, hi = 0, 0
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0


sol = Solution()
assert sol.checkValidString("()") is True
assert sol.checkValidString("(*)") is True
assert sol.checkValidString("(*))") is True
assert sol.checkValidString("(((") is False
print("All tests passed")

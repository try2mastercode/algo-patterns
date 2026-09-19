class Solution:
    def isValid(self, s):
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack


sol = Solution()
assert sol.isValid("()") is True
assert sol.isValid("()[]{}") is True
assert sol.isValid("(]") is False
assert sol.isValid("(") is False
assert sol.isValid("") is True
print("All tests passed")

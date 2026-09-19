class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        longest = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])
        return longest


sol = Solution()
assert sol.longestValidParentheses("(()") == 2
assert sol.longestValidParentheses(")()())") == 4
assert sol.longestValidParentheses("") == 0
print("All tests passed")

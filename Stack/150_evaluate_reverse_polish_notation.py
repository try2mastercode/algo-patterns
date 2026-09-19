class Solution:
    def evalRPN(self, tokens):
        stack = []
        for tok in tokens:
            if tok not in ("+", "-", "*", "/"):
                stack.append(int(tok))
            else:
                b = stack.pop()
                a = stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]


sol = Solution()
assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
print("All tests passed")

class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        digits = str(abs(x))[::-1]
        res = sign * int(digits)
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res


sol = Solution()
assert sol.reverse(123) == 321
assert sol.reverse(-123) == -321
assert sol.reverse(120) == 21
assert sol.reverse(1534236469) == 0
print("All tests passed")

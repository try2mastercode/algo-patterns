class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n

        def fast_pow(base, exp):
            if exp == 0:
                return 1
            half = fast_pow(base, exp // 2)
            return half * half * (base if exp % 2 else 1)

        return fast_pow(x, n)


sol = Solution()
assert sol.myPow(2.0, 10) == 1024.0
assert abs(sol.myPow(2.1, 3) - 9.261) < 1e-9
assert sol.myPow(2.0, -2) == 0.25
print("All tests passed")

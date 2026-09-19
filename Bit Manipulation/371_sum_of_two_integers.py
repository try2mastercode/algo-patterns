class Solution:
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        a &= mask
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        return a


sol = Solution()
assert sol.getSum(1, 2) == 3
assert sol.getSum(2, 3) == 5
assert sol.getSum(-2, 3) == 1
assert sol.getSum(-1, -1) == -2
print("All tests passed")

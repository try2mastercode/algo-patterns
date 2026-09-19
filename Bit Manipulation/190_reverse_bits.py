class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << (31 - i)
        return res


sol = Solution()
assert sol.reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000
assert sol.reverseBits(0b11111111111111111111111111111101) == 0b10111111111111111111111111111111
assert sol.reverseBits(0) == 0
print("All tests passed")

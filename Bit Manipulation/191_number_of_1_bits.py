class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


sol = Solution()
assert sol.hammingWeight(0b00000000000000000000000000001011) == 3
assert sol.hammingWeight(0b00000000000000000000000010000000) == 1
assert sol.hammingWeight(0) == 0
print("All tests passed")

class Solution:
    def plusOne(self, digits):
        digits = digits[:]
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


sol = Solution()
assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
assert sol.plusOne([9, 9]) == [1, 0, 0]
print("All tests passed")

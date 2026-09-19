class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1
        return []


sol = Solution()
assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert sol.twoSum([2, 3, 4], 6) == [1, 3]
assert sol.twoSum([-1, 0], -1) == [1, 2]
print("All tests passed")

class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


sol = Solution()
assert sol.containsDuplicate([1, 2, 3, 4, 5, 1]) is True
assert sol.containsDuplicate([1, 2, 3, 4]) is False
assert sol.containsDuplicate([]) is False
assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
print("All tests passed")

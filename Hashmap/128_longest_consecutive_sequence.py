class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


sol = Solution()
assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
assert sol.longestConsecutive([]) == 0
assert sol.longestConsecutive([1]) == 1
print("All tests passed")

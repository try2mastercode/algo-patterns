import bisect


class Solution:
    def lengthOfLIS(self, nums):
        tails = []
        for num in nums:
            i = bisect.bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)


sol = Solution()
assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert sol.lengthOfLIS([7, 7, 7, 7]) == 1
print("All tests passed")

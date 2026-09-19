from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        res = []
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


sol = Solution()
assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert sol.maxSlidingWindow([1], 1) == [1]
assert sol.maxSlidingWindow([9, 11], 2) == [11]
print("All tests passed")

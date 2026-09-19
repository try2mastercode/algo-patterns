class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        l, r = 0, m - 1
        while True:
            i = (l + r) // 2 if m > 0 else -1
            j = half - i - 2
            left1 = nums1[i] if i >= 0 else float("-inf")
            right1 = nums1[i + 1] if i + 1 < m else float("inf")
            left2 = nums2[j] if j >= 0 else float("-inf")
            right2 = nums2[j + 1] if j + 1 < n else float("inf")
            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1


sol = Solution()
assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert sol.findMedianSortedArrays([], [1]) == 1.0
assert sol.findMedianSortedArrays([2], []) == 2.0
print("All tests passed")

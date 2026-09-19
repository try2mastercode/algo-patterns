from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == need:
            return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            left = s2[i - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == need:
                return True
        return False


sol = Solution()
assert sol.checkInclusion("ab", "eidbaooo") is True
assert sol.checkInclusion("ab", "eidboaoo") is False
assert sol.checkInclusion("adc", "dcda") is True
assert sol.checkInclusion("abc", "ab") is False
print("All tests passed")

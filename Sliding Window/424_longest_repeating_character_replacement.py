class Solution:
    def characterReplacement(self, s, k):
        freq = {}
        l = 0
        max_freq = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


sol = Solution()
assert sol.characterReplacement("ABAB", 2) == 4
assert sol.characterReplacement("AABABBA", 1) == 4
assert sol.characterReplacement("A", 0) == 1
print("All tests passed")

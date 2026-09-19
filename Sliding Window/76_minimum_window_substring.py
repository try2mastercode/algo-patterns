from collections import Counter


class Solution:
    def minWindow(self, s, t):
        if not t or len(t) > len(s):
            return ""
        need = Counter(t)
        window = {}
        have, need_count = 0, len(need)
        res, res_len = [-1, -1], float("inf")
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            while have == need_count:
                if (r - l + 1) < res_len:
                    res, res_len = [l, r], r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""


sol = Solution()
assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert sol.minWindow("a", "a") == "a"
assert sol.minWindow("a", "aa") == ""
assert sol.minWindow("a", "b") == ""
print("All tests passed")

class Solution:
    def numberOfSubstrings(self, s):
        count = {"a": 0, "b": 0, "c": 0}
        left = 0
        total = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                count[s[left]] -= 1
                left += 1
            total += left
        return total


sol = Solution()
assert sol.numberOfSubstrings("abcabc") == 10
assert sol.numberOfSubstrings("aaacb") == 3
assert sol.numberOfSubstrings("abc") == 1
print("All tests passed")

class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]


sol = Solution()
assert sol.wordBreak("leetcode", ["leet", "code"]) is True
assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
print("All tests passed")

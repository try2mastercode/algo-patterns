from collections import deque, defaultdict
import string


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words = set(wordList)
        if endWord not in words:
            return 0

        patterns = defaultdict(list)
        words.add(beginWord)
        for word in words:
            for i in range(len(word)):
                patterns[word[:i] + "*" + word[i + 1:]].append(word)

        visited = {beginWord}
        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                for nei in patterns[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))
        return 0


sol = Solution()
assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
assert sol.ladderLength("a", "c", ["a", "b", "c"]) == 2
print("All tests passed")

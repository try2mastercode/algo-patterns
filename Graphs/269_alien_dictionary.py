class Solution:
    def alienOrder(self, words):
        graph = {ch: set() for word in words for ch in word}

        for w1, w2 in zip(words, words[1:]):
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].add(c2)
                    break

        state = {}  # 0=visiting, 1=done
        order = []

        def dfs(ch):
            if ch in state:
                return state[ch] == 1
            state[ch] = 0
            for nxt in graph[ch]:
                if not dfs(nxt):
                    return False
            state[ch] = 1
            order.append(ch)
            return True

        for ch in graph:
            if not dfs(ch):
                return ""
        return "".join(reversed(order))


sol = Solution()
assert sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
assert sol.alienOrder(["z", "x"]) == "zx"
assert sol.alienOrder(["z", "x", "z"]) == ""
print("All tests passed")

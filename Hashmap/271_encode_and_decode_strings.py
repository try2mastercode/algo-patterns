class Solution:
    def encode(self, strs):
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            res.append(s[start:start + length])
            i = start + length
        return res


sol = Solution()
assert sol.decode(sol.encode(["neet", "code", "love", "you"])) == ["neet", "code", "love", "you"]
assert sol.decode(sol.encode([""])) == [""]
assert sol.decode(sol.encode([])) == []
assert sol.decode(sol.encode(["a#b", "5#c"])) == ["a#b", "5#c"]
print("All tests passed")

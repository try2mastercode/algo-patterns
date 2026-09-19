class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())


def normalize(groups):
    return sorted(sorted(g) for g in groups)


sol = Solution()
assert normalize(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == normalize(
    [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
)
assert sol.groupAnagrams([""]) == [[""]]
assert sol.groupAnagrams(["a"]) == [["a"]]
print("All tests passed")

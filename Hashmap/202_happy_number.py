class Solution:
    def isHappy(self, n):
        def next_n(x):
            return sum(int(d) ** 2 for d in str(x))

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_n(n)
        return n == 1


sol = Solution()
assert sol.isHappy(19) is True
assert sol.isHappy(2) is False
assert sol.isHappy(1) is True
assert sol.isHappy(7) is True
print("All tests passed")

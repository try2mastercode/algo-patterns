from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        max_count = max(counts.values())
        num_max = sum(1 for c in counts.values() if c == max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + num_max)


sol = Solution()
assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
assert sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
print("All tests passed")

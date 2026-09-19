from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, point):
        self.counts[tuple(point)] += 1

    def count(self, point):
        px, py = point
        total = 0
        for (x, y), cnt in self.counts.items():
            if x == px or abs(x - px) != abs(y - py):
                continue
            total += cnt * self.counts.get((x, py), 0) * self.counts.get((px, y), 0)
        return total


ds = DetectSquares()
ds.add([3, 10])
ds.add([11, 2])
ds.add([3, 2])
assert ds.count([11, 10]) == 1
assert ds.count([14, 8]) == 0
ds.add([11, 2])
assert ds.count([11, 10]) == 2
print("All tests passed")

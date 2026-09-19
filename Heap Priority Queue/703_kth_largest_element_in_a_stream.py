import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


kl = KthLargest(3, [4, 5, 8, 2])
assert kl.add(3) == 4
assert kl.add(5) == 5
assert kl.add(10) == 5
assert kl.add(9) == 8
assert kl.add(4) == 8
print("All tests passed")

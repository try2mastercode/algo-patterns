from collections import Counter
import heapq


class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        heap = list(counts.keys())
        heapq.heapify(heap)
        while heap:
            first = heap[0]
            for card in range(first, first + groupSize):
                if counts[card] == 0:
                    return False
                counts[card] -= 1
                if counts[card] == 0:
                    if card != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True


sol = Solution()
assert sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
assert sol.isNStraightHand([1, 2, 3, 4, 5], 4) is False
assert sol.isNStraightHand([1, 1, 2, 2, 3, 3], 3) is True
print("All tests passed")
